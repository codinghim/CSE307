fun cycle(input) = tl(input) @ [hd(input)];

val list = [1,2,3];
val list2 = ["a","b","c"];

cycle(list);
cycle(list2);