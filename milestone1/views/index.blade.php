<!DOCTYPE html>
<html lang="{{ str_replace('_', '-', app()->getLocale()) }}">
    <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1">

        <title>ETDsearch</title>

        <!-- Fonts -->
        <link href="https://fonts.googleapis.com/css2?family=Nunito:wght@400;600;700&display=swap" rel="stylesheet">

        <script src="https://kit.fontawesome.com/a076d05399.js"></script>
        <link rel="stylesheet" href="/css/style.css">


    </head>
    <body class="antialiased">
        <div class="relative flex items-top justify-center min-h-screen bg-gray-100 dark:bg-gray-900 sm:items-center sm:pt-0">
            @if (Route::has('login'))
                <div class="hidden fixed top-0 right-0 px-6 py-4 sm:block">
                    @auth
                        <a href="{{ url('/home') }}" class="text-sm text-gray-700 underline">Home</a>
                    @else

                        <!-- perosnal code start -->
                        <a href="{{ url('/') }}" class="text-sm text-gray-700 underline">Home</a>
                        <!-- perosnal code end -->

                        <a href="{{ route('login') }}" class="text-sm text-gray-700 underline">Login</a>

                        @if (Route::has('register'))
                            <a href="{{ route('register') }}" class="ml-4 text-sm text-gray-700 underline">Register</a>
                        @endif
                    @endif
                </div>
            @endif


<!-- Personal comments start:  inserting my code-->

            <div class="wrap">
               <div class="search">
                  <input type="text" class="searchbox" placeholder="What are you looking for?">
                  <button type="submit" class="searchButton">
                  <i class="fa fa-search"></i>
                  </button>
               </div>
            </div>

<!-- Personal comments end-->


            </div>
        </div>
    </body>
</html>
