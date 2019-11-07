fun self(input) = input;
fun inc(input) = input + 1;
fun double(input) = input * 2;



fun hiF(f, a) = if null(f) andalso null(a) then nil
    else (hd(a), hd(f)(hd(a))) :: hiF(tl(f),tl(a));

val a = [1,2,3];
val b = [self, inc, double];

hiF(b,a);