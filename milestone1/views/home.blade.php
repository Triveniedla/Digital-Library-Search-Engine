@extends('layouts.app')

@section('content')
<script type="text/javascript" src="https://ajax.googleapis.com/ajax/libs/jquery/3.2.1/jquery.min.js"></script>
<div class="wrap">
   <div class="search">
      <input type="text" class="searchbox" placeholder="What are you looking for?">
      <button type="submit" class="searchButton">
      <i class="fa fa-search"></i>
      </button>

      <br><br>
      <!-- <a href="{{ url('/advancesearch') }}" class="text-sm text-gray-700 underline">Advance search</a> -->
      </div>


      <button type="button" id="formButton">Advance Search!</button>

       <form id="form1">
         <b>Author:</b> <input type="text" name="firstName">
         <br><br>
         <b>Title: </b><input type="text" name="lastName">
         <br><br>
         <b>University: </b><input type="text" name="lastName">
         <br><br>
         <b>Published in(Year): </b><input type="text" name="lastName">
         <br><br>
         <button type="button" id="submit">Submit</button>
       </form>
<script>
$(document).ready(function() {
  $("#formButton").click(function() {
    $("#form1").toggle();
  });
});
</script>
</div>

<!-- Personal comments: End -->


@endsection
