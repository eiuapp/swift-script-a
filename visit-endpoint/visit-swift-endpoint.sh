#!/bin/bash

# curl -v -H 'X-Auth-Token: 8533cb3873974fa29f03832aef7007ca' http://192.168.0.50:8080/v1/AUTH_a640c74e595c44c4902d1c5ebc3afa8a

user=$1
echo $user
if [[ $user == "demo" ]] ; then
    echo "for demo: \n"
    publicURL='http://192.168.0.50:8080/v1/AUTH_7d6eaa90d74a4f239963933c3a744df3'
    token='gAAAAABcQFexnMtRH_tE8XQBfA5bNi5egDaeJupSAwXEeSbvfMFMcXCas2t5z0PVWrEW7fEQ3zWyWf_dsrZedLOiqv1LONUxH1Z3HNeg-Ne17LtygLU6HXuZs_fXw0KrSFqxHloqMIwK0N8zpjsDi0hxyL5Jthp28PH_YDYrxSudFeM9f47PhJ8'
    token='gAAAAABcQG-BuDOfcrb7f62QZNJAp_Tvq32SDvCRinw36yfN0QJz_FFCiApYWeMxeb6jFECdEYOkbFFi06uMfhsVtykkQMnzQAsSeH-K7sFe1s_E24n0d93SNrGP4SWOa4Abb1_CsJACKthZwJWEOSouM9n8DoNYWCQATcro0_wAuR4PjklhdZc'
    token='gAAAAABcQG_B-Tm7g8wfycSBHROCIYlNLyPjXs-ccQ2LwAuvaS13VvG4hxf_nu77ZWrOvIof7GzArK9eYJOD36q4Uw6m4RP5s9qi1AzDTBefckN0unJw51gT0gdtE5e633r30QcnC32ERS7CnRarNB0gr8DEOI_mNw'
    token='gAAAAABcQVk7Q6QgnbTmTobnt36rLZmifbCMow4W-MWfQ9txcRyHEYOPXWRKAcc2r7bAVG0uS_VNC5GyIPw6FjQx3Bb-mofESZDEPs5AHe8m2Pg1Nwfmhrd8lg_4VqWZRffUQIrrRiNH1JSViBXFRZJn0zwSdwUREoskIuetQ0uZ5FWXuQOz240'
elif [[ $user == "admin" ]] ; then
    echo "for admin: \n"
    publicURL='http://192.168.0.50:8080/v1/AUTH_f04ec0abf3d1460dad82608bb03af589'
    token='gAAAAABcQFxoK2-kH-z2NcevICCi6kSJa3Xjd5azSK3ib_Ao3ZYARuL8IJTo91_vIvttlYR6dwPkZyyAtIhOwElK86Ixqos6MBF_Vg-E_3zGsKt-o5IjmEX97E3b2eY7aWndpXgh34h0UaQ8RY7lBkB4Gm3BOHATzVnibTJdNysZfjyxN7-1_fU'
elif [[ $user == 'swift' ]] ; then
    echo "Statement(s) to be executed if expression 3 is true"
else
    echo "Statement(s) to be executed if no expression is true"
fi

echo $publicURL
echo $token
echo 'curl -i $publicURL?format=json -X GET -H "X-Auth-Token: $token" # | python -mjson.tool'
curl -i $publicURL?format=json -X GET -H "X-Auth-Token: $token" # | python -mjson.tool

# curl -i http://192.168.0.50:8080/v1/AUTH_7d6eaa90d74a4f239963933c3a744df3?format=json -X GET -H "X-Auth-Token: gAAAAABcQFexnMtRH_tE8XQBfA5bNi5egDaeJupSAwXEeSbvfMFMcXCas2t5z0PVWrEW7fEQ3zWyWf_dsrZedLOiqv1LONUxH1Z3HNeg-Ne17LtygLU6HXuZs_fXw0KrSFqxHloqMIwK0N8zpjsDi0hxyL5Jthp28PH_YDYrxSudFeM9f47PhJ8"
curl -i http://192.168.0.50:8080/v1/AUTH_7d6eaa90d74a4f239963933c3a744df3?format=json -X GET -H "X-Auth-Token: gAAAAABcQVk7Q6QgnbTmTobnt36rLZmifbCMow4W-MWfQ9txcRyHEYOPXWRKAcc2r7bAVG0uS_VNC5GyIPw6FjQx3Bb-mofESZDEPs5AHe8m2Pg1Nwfmhrd8lg_4VqWZRffUQIrrRiNH1JSViBXFRZJn0zwSdwUREoskIuetQ0uZ5FWXuQOz240"
