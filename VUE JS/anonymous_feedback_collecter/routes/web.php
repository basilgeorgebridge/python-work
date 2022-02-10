<?php



//API
$router->group(['prefix' => 'api/v1'],  function () use ($router) {
    $router->post('register' , 'UserController@register');
    $router->post('login' , 'UserController@login');
    $router->get('logout' , 'UserController@logout');
    $router->post('forgot-password', 'UserController@sendEmail');
    $router->post('reset-password', 'UserController@passwordResetProcess');
    $router->post('/review/create', 'ReviewsController@store' );
} ); 

$router->group(['prefix' => 'api/v1' , 'middleware' => 'auth'],  function () use ($router) {
    $router->get('/me', 'UserController@me');
    $router->get('/refresh', 'UserController@refresh');

 });


$router->group(['prefix' => 'api/v1/user' , 'middleware' => 'auth'],  function () use ($router) {
    $router->post('/change-password', 'UserController@PasswordChangeProcess' );
    $router->get('/groups[/{id}]', 'GroupController@index' ); //wildcardaccepts  
    $router->get('/reviews', 'ReviewsController@index' );
    $router->post('/group/create', 'GroupController@store' );
 });

//delete this
$router->get('/reviews', 'ReviewsController@f' );

//UI
$router->get('view', function () {
    return view('login', ['name' => 'James']);
});