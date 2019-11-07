fun fib(input:int) = if(input = 0) then 0
    else if (input = 1) then 1
    else fib(input - 1) + fib(input - 2);

fib(1);
fib(2);
fib(3);
fib(4);
fib(5);
fib(6);
fib(20);
fib(40);

(* The smallest value to cause the uncaught exception Overflow is 45. *)
