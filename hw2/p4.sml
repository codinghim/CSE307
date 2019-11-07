fun one(L) =
    if L = nil then nil
    else hd(L):: three(tl(L))

and
    two(L) = 
    if L = nil then nil
    else one(tl(L))

and
    three(L) =
    if L = nil then nil
    else two(tl(L));

val list = [1,2,3];
val list2 = [1,2,3,4,5,6];

one(list);
two(list);
three(list);
one(list2);
two(list2);
three(list2);
