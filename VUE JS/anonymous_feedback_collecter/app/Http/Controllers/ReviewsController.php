<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;
use App\Models\Review;
use App\Models\User;
use App\Models\Groups;
use App\Http\Controllers\ResponseController;
use Illuminate\Pagination\Paginator;
use Symfony\Component\HttpFoundation\Response;

class ReviewsController extends ResponseController
{
    public function f(){
        $reviews = Review::all();
        return $this->responseFn($reviews);
    }
    public function index(Request $request)
    {
        
        $from_date = date_create();
        $to_date = date_format($from_date,"Y-m-d");
        date_add($from_date,date_interval_create_from_date_string("-30 days"));
        $from_date = date_format($from_date,"Y-m-d");
        if( $request->input('from_date')){
            $from_date = $request->input('from_date');
         }
        
        if( $request->input('to_date')){
            $to_date = $request->input('to_date');
         }
        
        $sort = 'asc';//asc or desc else sql error
        if( $request->input('sort') == 'asc' || $request->input('sort') == 'desc' ){
            $sort = $request->input('sort');
        }else if( $request->input('sort') ){
            return $this->responseHttp([
                'error' => 'Sorting keyword is incorrect.'
            ], 404);
        }
        
        $per_page = 5;
        if( $request->input('per_page')){
            $per_page = $request->input('per_page');
        }
        $groups_id = [];
        if( $request->input('groups_id') ){
            $groups_id[] = $request->input('groups_id');
        }else{
            $groups = User::find( auth()->user()->id )->getGroups;
            foreach( $groups as $group){
                array_push( $groups_id, $group->id );
            }     
        }
        // not used has many     
        $reviews = Review::whereIn('groups_id', $groups_id)->whereDate('created_at','<=',$to_date)->whereDate('created_at','>=',$from_date)->orderBy( 'created_at' , $sort )->paginate( $per_page );
        $data = [];
        foreach( $reviews as $review ){
            $group_name = Groups::where('id', '=', $review->groups_id)->get();
            $data[] = ["id"=>$review->id,  "review"=>$review->review, "group_name"=>$group_name[0]->name,"created_at"=>Date($review->created_at)];
        }
        return $this->responseFn(["reviews"=>$data, "current_page"=>$reviews->currentPage(),"last_page" => $reviews->lastPage()]);
        
    }

    public function store(Request $request)
    {
        $this->validate( $request, [
            'review' => 'required',
            'url_id' => 'required'
        ]);
        $review = new Review();
        $groups =  Groups::where('url_id','=', $request->input('url_id')  )->get();
        if( count( $groups ) == 1){
            $review->review = $request->input('review');
            $review->groups_id = $groups[0]->id;
            $review->save();
            return $this->responseFn($review);
        }else{

            return $this->responseHttp([
                'error' => 'group id is Incorrect'
            ], 404);
        }

        
    }

}







   
// public function update(Request $request, $id)
// {
//     $this->validate( $request, [
//         'review' => 'required',
//         'group_id' => 'required'
//     ]);
//     $review = Review::find( $id );
//     $review->review = $request->input('review');
//     $review->group_id = $request->input('group_id');
//     $review->save();
//     return $this->responseFn($review);
// }
