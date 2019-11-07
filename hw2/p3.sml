fun duplicate(input) = if null(input) then nil
    else [hd(input)] @ [hd(input)] @ duplicate(tl(input));

val list = [1,2,3];
val list2 = ["a","b","c"];

duplicate(list);
duplicate(list2);