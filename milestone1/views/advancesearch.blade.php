@extends('layouts.app')

@section('content')


<div class="advsearchbox">

  <label for="booktitle"><b>Title</b></label><br>
  <input type="text" placeholder="Title" name="booktitle" required><br><br>

  <label for="bookauthor"><b>book Author</b></label><br>
  <input type="text" placeholder="Book author" name="bookauthor" required><br><br>

</div>


@endsection
