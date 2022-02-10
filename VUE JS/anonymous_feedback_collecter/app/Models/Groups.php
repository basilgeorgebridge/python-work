<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Model;

class Groups extends Model
{
    protected $fillable=[
        'name', 'description', 'user_id', 'url_id'
    ];

    function getReviews(){
        return $this->hasMany(Review::Class);
    }
 
}
