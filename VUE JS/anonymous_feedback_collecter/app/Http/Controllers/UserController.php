<?php

namespace App\Http\Controllers;

use Illuminate\Support\Facades\Auth;
use App\Models\User;
use App\Http\Controllers\Controller;
use Illuminate\Http\Request;
use Illuminate\Support\Facades\Hash;
use Symfony\Component\HttpFoundation\Response;
use App\Mail\SendMailReset;
use Illuminate\Support\Facades\Mail;
use Carbon\Carbon;
use Illuminate\Support\Facades\DB;
use Illuminate\Support\Str;
use App\Http\Controllers\ResponseController;

class UserController extends ResponseController
{
    public function __construct()
    {
        $this->middleware('auth:api', ['except' => ['register','login', 'sendEmail','send','createToken','saveToken','validateEmail','failedResponse','successResponse','passwordResetProcess']]);
    }

    public function login(Request $request)
    {
        $this->validate( $request, [
            'email' => 'required',
            'password' => 'required'
        ]);

        $credentials = $request->only(['email', 'password']);

        if (! $token = auth()->attempt($credentials)) {
            return $this->responseHttp(['error' => 'Unauthorized'], 401);
        }
        return $this->respondWithToken($token);
    }

  
 
    public function logout()
    {
        auth()->logout();
        return response()->json(['message' => 'Successfully logged out']);
    }


    public function refresh()
    {
        return $this->respondWithToken(auth()->refresh());
    }
    public function me()
    {
        return response()->json([
            'success' => true,
            'data' => auth()->user()
        ]);
    }
 
    
    //psdReset
    public function sendEmail(Request $request)  // this is most important function to send mail and inside of that there are another function
    {
        if (!$this->validateEmail($request->email)) {  // this is validate to fail send mail or true
            return $this->failedResponse();
        }
        $this->send($request->email);  //this is a function to send mail 
        return $this->successResponse();
    }

    public function send($email)  //this is a function to send mail 
    {
        $token = $this->createToken($email);
        Mail::to($email)->send(new SendMailReset($token, $email));  // token is important in send mail 
    }

    public function createToken($email)  // this is a function to get your request email that there are or not to send mail
    {
        $oldToken = DB::table('password_resets')->where('email', $email)->first();

        if ($oldToken) {
            return $oldToken->token;
        }

        $token = Str::random(40);
        $this->saveToken($token, $email);
        return $token;
    }


    public function saveToken($token, $email)  // this function save new password
    {
        DB::table('password_resets')->insert([
            'email' => $email,
            'token' => $token,
            'created_at' => Carbon::now()
        ]);
    }
    public function validateEmail($email)  //this is a function to get your email from database
    {
        return !!User::where('email', $email)->first();
    }

    public function failedResponse()
    {
        return $this->responseHttp([
            'error' => 'Email doesn\'t found on our database'
        ], Response::HTTP_NOT_FOUND);
    }

    public function successResponse()
    {
        return $this->responseHttp([
            'data' => 'Reset Email is send successfully, please check your inbox.'
        ], Response::HTTP_OK);
    }
    //change password
    public function PasswordChangeProcess(Request $request){
        
        $this->validate($request, [
            'current_password' => 'required',
            'password' => 'required|confirmed'
        ]);
       
        if(Hash::check($request->input('current_password'), auth()->user()->password)) {     
            $user = User::find(auth()->user()->id);
            $user->password = Hash::make( $request->input('password'));
            $user->save();
            return $this->responseFn($user);
        }else{
            return $this->responseFn("current password is not matching");
        }
    }
//signup
    public function register(Request $request){
        $this->validate($request, [
            'name' => 'required',
            'email' => 'required|unique:users,email,1,id',
            'password' => 'required|confirmed'
        ]);
        $name = $request->input('name'); 
        $email = $request->input('email'); 
        $password = Hash::make( $request->input('password') );
        User::create(['name' => $name,'email' => $email, 'password' => $password ]);
        return $this->responseFn(['status' => 'Registered successfully', 'opertaion'=> 'created']);
        
    }

    public function passwordResetProcess(Request $request){
        
        $this->validate($request, [
            'resetToken' => 'required',
            'email' => 'required',
            'password' => 'required|confirmed'
        ]);

        $password_resets = DB::table('password_resets')->where([
            'token' => $request->input('resetToken')
        ])->get();
        if( count( $password_resets ) > 0 ){// recheck $password_resets is array or not
            if( $request->input('email') == $password_resets[0]->email ){
                echo "entered email is matching\n";
                DB::table('users')
                ->where('email', '=', $password_resets[0]->email )
                ->update(['password' => Hash::make( $request->input('password'))]);
                return $this->responseFn("updated successfully"); // if any error still show updated successfully  
            }else{
                return $this->responseFn("entered email not macthing");
                
            }
        }else{
            return $this->responseFn("Entered token is invalid");
             
        }
    }


}