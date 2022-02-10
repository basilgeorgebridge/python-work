<?php

namespace App\Http\Controllers;
use Symfony\Component\HttpFoundation\Response;

class ResponseController extends Controller
{
    public function responseFn($result)
    {
        return response()->json($result);
    }
    public function responseHttp($msg, $httpResponse){
        return response()->json($msg, $httpResponse);
    }



    
    protected function respondWithToken($token)
    {
        return response()->json([
            'email' => auth()->user()->email,
            'access_token' => $token,
            'token_type' => 'Bearer',
            'expires_in' => auth()->factory()->getTTL() * 120000000000000000000
        ]);
    }
}
