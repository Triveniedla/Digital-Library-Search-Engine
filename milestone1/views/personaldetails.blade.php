@extends('layouts.app')

@section('content')


<div style="background-color:white" class="container">

   <h1>Update account details</h1>
<form class="" method ="GET" action="{{URL('updateProfile')}}">
   <label for="fname"><b>Name</b></label><br>
   <p>{{Auth::user()->name}}</p>
   <label for="email"><b>Email</b></label><br>
   <input type = "hidden" name = "email" value = "{{Auth::user()->email}}" />
   <p>{{Auth::user()->email}}</p>
   <label for="pwd"><b>Password</b></label><br>
   <input type = "hidden" name = "email" value = "{{Auth::user()->password}}" />

   @if (Route::has('password.request'))
       <a class="btn btn-link" href="{{ route('password.request') }}">
           {{ __('Change your Password') }}
       </a>
   @endif
 </form>
</div>


@endsection
