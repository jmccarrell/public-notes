#!/usr/bin/env zsh

function rev () {
    declare -a out
    while (( $# > 0 )); do
        s=$1; shift
        # split $1 on character boundaries
        declare -a source=(${(ps..)s})
        declare -a result=()
        while (( $#source > 0 )); do
            result+=($source[-1])
            shift -p source
        done;
        # join the result array back down to a string
        r=${(j::)result}
        out+=($r)
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
