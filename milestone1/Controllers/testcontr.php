<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;
use App\Models\User;

class testcontr extends Controller
{

  function index(User $key)
  {
    return $key;
  }
    //
}
