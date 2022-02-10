<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;
use App\Models\Groups;
use App\Models\Review;
use App\Http\Controllers\ResponseController;
use Illuminate\Pagination\Paginator;

class GroupController extends ResponseController
{
   
    public function index(Request $request,$id = null)
    {   
        $where = [['user_id', '=', auth()->user()->id]];
        if( $request->input('group_name') != ''){
           $where[] = ['name', 'LIKE', "%{$request->input('group_name')}%"];
        }else if($id){
            $where[] = ['id', '=', $id];
        }       
        $per_page = 6;
        if( $request->input('per_page') != null || $request->input('per_page') != '' ){
            $per_page = $request->input('per_page');
        }
        $num_reviews = [];
        $groups = Groups::where( $where )->paginate( $per_page ); //contain an array[{},{}]
        foreach($groups as $group){
            $num_review =  Groups::find($group->id)->getReviews->count();
            $num_reviews[] = ["group_id"=>$group->id,"name"=>$group->name,"description"=>$group->description,"url_id"=>$group->url_id, "num_of_reviews"=>$num_review];
        }       
        return $this->responseFn([["current_page"=>$groups->currentPage(),"last_page" => $groups->lastPage(),"groups_per_page"=>$groups->count()],["groups"=>$num_reviews]] );
    }

    public function store(Request $request)
    {
        $this->validate( $request, [
            'name' => 'required',
            'description' => 'required'
        ]);
        $group = new Groups();
        $mismatch = Groups::where([['name', '=', $request->input('name')],['user_id', '=', auth()->user()->id]] )->get();
        if( count( $mismatch ) != 0 ){
            return $this->responseHttp(["msg" => "Group name already exist"], 409);
        }
        $group->name = $request->input('name');
        $group->description = $request->input('description');
        $group->user_id = auth()->user()->id;
        $group->url_id = "GID".strval( rand(10,100) )."A".strval( rand(100,10000) );// automatically create group_id
        $group->save();
        return $this->responseFn($group);
    }

   
    public function update(Request $request, $id)
    {
        $this->validate( $request, [
            'name' => 'required',
            'description' => 'required',
            'user_id' => 'required',
            'url_id' => 'required'
        ]);
        $group = Groups::find( $id );
        $group->name = $request->input('name');
        $group->description = $request->input('description');
        $group->user_id = $request->input('user_id');
        $group->url_id = $request->input('url_id');
        $group->save();
        return $this->responseFn($group);
    }

  
    public function destroy($id)
    {
        $group = Groups::find( $id );
        $group->delete();
        return $this->responseFn("Group deleted successfully");
    }


}
