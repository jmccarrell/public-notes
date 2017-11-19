#!/usr/bin/env zsh

function rev () {
    declare -a out=()
    while (($# > 0)); do
        # split $1 on character boundaries
        declare -a source=(${(ps..)1})
        shift
        declare -a result=()
        while (($#source > 0)); do
            result+=($source[-1])
            shift -p source
        done;
        # join the result array back down to a string
        out+=(${(j::)result})
    done
    print $out
    return 0
}

function show_rev() {
    print "$#:" $@
    print '>>' $(rev $@)
}
declare -a egbdf=(every good boy does fine)
show_rev $egbdf
show_rev "$egbdf"
declare -a racing_emoji=(racing_car_🏎 racing_motorcycle_🏍 horse_racing_🏇)
show_rev $racing_emoji
show_rev "$racing_emoji"
# the empty string
show_rev
