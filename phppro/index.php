<?php
require_once 'conn.php';
if(ISSET($_POST['add'])){
    if($_POST['task'] != ""){
        $task = $_POST['task'];

        $conn->query("INSERT INTO `task` VALUES('', '$task', '')");
        header('location:index.php');
    }
}
?>










<!doctype html>
<html lang="en">
  <head>
    <!-- Required meta tags -->
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">

    <!-- Bootstrap CSS -->
    <link href="https://stackpath.bootstrapcdn.com/bootstrap/4.2.1/css/bootstrap.min.css" rel="stylesheet"/>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta2/css/all.min.css" integrity="sha512-YWzhKL2whUzgiheMoBFwW8CKV4qpHQAEuvilg9FAn5VJUDwKZZxkJNuGM4XkWuk94WCrrwslk8yWNGmY1EduTA==" crossorigin="anonymous" referrerpolicy="no-referrer" />
    <link rel="stylesheet" href="./css/style.css" />
    <title>The todo app!</title>
  </head>
  <body>
    <section class="vh-100">
    <div class="container py-5 h-100">
        <div class="row d-flex justify-content-center align-items-center h-100">
        <div class="col">
            <div class="card" id="list1" style="border-radius: .75rem; background-color: #eff1f2;">
            <div class="card-body py-4 px-4 px-md-5">
    
                <p class="h1 text-center mt-3 mb-4 pb-3 text-primary"><i class="fas fa-check-square me-1"></i> Simple Todo App</p>
                
                <!-- Todo Area -->
                <form method="POST">
                <div class="pb-2">
                <div class="card">
                    <div class="card-body">
                    <div class="d-flex flex-row align-items-center">
                        <input type="text" class="form-control form-control-lg" id="exampleFormControlInput1" placeholder="Add new...">
                        <div>
                        <button type="button" class="btn btn-primary">Add</button>
                        </div>
                    </div>
                    </div>
                </div>
                </div>
    
                <hr class="my-4">
                <!-- Filters -->
                <div class="clearfix">
                <div class="d-flex justify-content-end align-items-center mb-4 pt-2 pb-3 w-20 float-right">
                <p class="small mb-0 me-2 text-muted">Filter: </p>
                <select class="form-control">
                    <option value="1">All</option>
                    <option value="2">Completed</option>
                    <option value="3">Active</option>
                </select>
                <a href="#!" style="color: #23af89;" data-mdb-toggle="tooltip" title="Ascending"><i class="fas fa-sort-amount-down-alt ms-2"></i></a>
                </div>
                </div>

                <!-- Existing data -->
                <ul class="list-group list-group-horizontal rounded-0 bg-transparent">
                <li class="list-group-item">
                    <div class="custom-control-lg custom-control custom-checkbox todo-item">
                        <input class="custom-control-input" id="checkbox-large" type="checkbox"/>
                        <label class="custom-control-label" for="checkbox-large">
                            My first static todo item!
                        </label>
                        <a href="#!" class="text-danger" data-mdb-toggle="tooltip" title="Delete todo"><i class="fas fa-trash-alt"></i></a>
                    </div>
                </li>
                </ul>
    
            </div>
            </div>
        </div>
        </div>
    </div>
      </section>
  </body>
</html>
