$(document).ready(function () {
    // var otp = '0123456789';

    // // otp generate
    // $("#otp").click(function (event) {
    //     event.preventDefault();
    //     if (($('#uname1').val() == 'basil') || ($('#uname1').val() == 'admin')) {
    //         otp = (Math.floor(Math.random() * 10000) + 10000).toString().substring(1);
    //         alert(otp);
    //     } else {
    //         alert("Enter valid Username");
    //         return false;
    //     }
    // })

    // $('div[for="chngspswd"]').hide()
    // $('input[for="otp"]').focusout(function () {
    //     $('div[for="chngspswd"]').show()
    // })
    // $('input[for="otp"]').focusin(function () {
    //     $('div[for="chngspswd"]').hide()
    // })

    // forgot password otp
    // $('input[for="otp"]').focusout(function () {
    //     if ($("#otp1").val() == otp) {
    //         window.location.href = 'profile.html';
    //         alert("change password")
    //         $('div[for="chngspswd"]').show()
    //     } else {
    //         alert("otp not valid");
    //         return false;
    //     }
    // })

    // fogotpassword validation
    // $("#otpsubmit").click(function () {
    //     var password = $("#npswd").val();
    //     var confirmPassword = $("#cpswd").val();
    //     if ((password != confirmPassword) && ($('#uname1').val() == 'basil')) {
    //         alert("Passwords do not match.");
    //         return false;
    //     } else if ((password != confirmPassword) && ($('#uname1').val() == 'admin')) {
    //         alert("Passwords do not match.");
    //         return false;
    //     } else {
    //         alert("Password changed Successfully")
    //         window.location.href = 'login.html';
    //     }
    // });


    // $("#otpsubmit").click(function () {
    //     if ($("#otp1").val() == otp) {
    //         window.location.href = 'profile.html';
    //         alert("change password")

    //     } else {
    //         alert("otp not valid");
    //         return false;
    //     }
    // })

    // loginpasswordchange
    // $("#cpswd").focusout(function (event) {
    //     event.preventDefault();
    //     var password = $("#npswd").val();
    //     var confirmPassword = $("#cpswd").val();
    //     if ((password != confirmPassword) || (password == '')) {
    //         alert("Passwords do not match.");
    //         return false;
    //     } else {
    //         alert("Password changed Successfully");
    //         window.location.href = 'login.html';
    //     }
    // });

    // user confirm password 
    // $("#conpswd1").click(function (event) {
    //     event.preventDefault();
    //     var password = $("#newpswd").val();
    //     var confirmPassword = $("#conpswd").val();
    //     if ((password != confirmPassword) || (password == '')) {
    //         alert("Passwords do not match.");
    //         return false;
    //     } else {
    //         alert("Password changed Successfully");
    //         window.location.href = 'profile.html';
    //     }
    // });

    // admin password check
    // $("#conpswd2").click(function () {
    //     var password = $("#newpswd").val();
    //     var confirmPassword = $("#conpswd").val();
    //     if ((password != confirmPassword) || (password == '')) {
    //         alert("Passwords do not match.");
    //         return false;
    //     } else {
    //         alert("Password changed Successfully");
    //         window.location.href = 'ad_profile.html';
    //     }
    // });

    // $("#cnflv").click(function () {
    //     alert("leave applied successfully");
    //     window.location.href = 'profile.html'
    // })
    // $("#adcnflv").click(function () {
    //     alert("leave applied successfully");
    //     window.location.href = 'ad_profile.html'
    // })

    // $("#lvstsdetbck").click(function () {
    //     window.location.href = 'leavestatus.html'
    // })
    // $("#lback").click(function () {
    //     window.location.href = 'login.html'
    // })

    // days
    // $('label[for="day"]').hide();
    // $('label[for="reason"]').click(function (event) {
    //     event.preventDefault();
    //     var fromday = $('input[value="from"]').val();
    //     var today = $('input[value="to"]').val();
    //     if (Date.parse(today) >= Date.parse(fromday)) {
    //         $('label[for="day"]').show();
    //     }
    // });
    // fullday/halfday
    // $('label[for="session"]').hide();
    // $('input[value="halfday"]').click(function () {
    //     $('label[for="session"]').show();
    // })
    // $('input[value="fullday"]').click(function () {
    //     $('label[for="session"]').hide();
    // })
    // // date validations

    function validateFromDate() {
        var today = new Date();
        var dd = String(today.getDate()).padStart(2, '0');
        var mm = String(today.getMonth() + 1).padStart(2, '0');
        var yyyy = today.getFullYear();

        today = yyyy + '-' + mm + '-' + dd;
        $('#from').attr('min', today);
    }
        // $("#otpsubmit").click(function () {
        //     if ($("#otp1").val() == otp) {
        //         window.location.href = 'profile.html';
        //         alert("change password")
    
        //     } else {
        //         alert("otp not valid");
        //         return false;
        //     }
        // })
    
        // loginpasswordchange
        // $("#cpswd").focusout(function (event) {
        //     event.preventDefault();
        //     var password = $("#npswd").val();
        //     var confirmPassword = $("#cpswd").val();
        //     if ((password != confirmPassword) || (password == '')) {
        //         alert("Passwords do not match.");
        //         return false;
        //     } else {
        //         alert("Password changed Successfully");
        //         window.location.href = 'login.html';
        //     }
        // });
    
        // user confirm password 
        // $("#conpswd1").click(function (event) {
        //     event.preventDefault();
        //     var password = $("#newpswd").val();
        //     var confirmPassword = $("#conpswd").val();
        //     if ((password != confirmPassword) || (password == '')) {
        //         alert("Passwords do not match.");
        //         return false;
        //     } else {
        //         alert("Password changed Successfully");
        //         window.location.href = 'profile.html';
        //     }
        // });
    
        // admin password check
        // $("#conpswd2").click(function () {
        //     var password = $("#newpswd").val();
        //     var confirmPassword = $("#conpswd").val();
        //     if ((password != confirmPassword) || (password == '')) {
        //         alert("Passwords do not match.");
        //         return false;
        //     } else {
        //         alert("Password changed Successfully");
        //         window.location.href = 'ad_profile.html';
        //     }
        // });
    
        // $("#cnflv").click(function () {
        //     alert("leave applied successfully");
        //     window.location.href = 'profile.html'
        // })
        // $("#adcnflv").click(function () {
        //     alert("leave applied successfully");
        //     window.location.href = 'ad_profile.html'
        // })
    
        // $("#hback").click(function () {
        //     window.location.href = 'home.html'
        // })
    
        // $("#lvstsdetbck").click(function () {
        //     window.location.href = 'leavestatus.html'
        // })
        // $("#lback").click(function () {
        //     window.location.href = 'login.html'
        // })
    
        // fullday/halfday

        $('label[for="day"]').hide();
        $("#to").focusout(function() {
            var fromday = $("#from").val();
            var today = $("#to").val(); 
            if(Date.parse(fromday) == Date.parse(today)){
                $('label[for="day"]').show();
            }
        });

        // first/secondhalf

        $('label[for="session"]').hide();
        $('input[value="halfday"]').click(function () {
            $('label[for="session"]').show();
        })
        $('input[value="fullday"]').click(function () {
            $('label[for="session"]').hide();
        })

        // // date validations
    
        function validateFromDate() {
            var today = new Date();
            var dd = String(today.getDate()).padStart(2, '0');
            var mm = String(today.getMonth() + 1).padStart(2, '0');
            var yyyy = today.getFullYear();
    
            today = yyyy + '-' + mm + '-' + dd;
            $('#from').attr('min', today);
        }
    
        $('#from').on('change', function () {
            var fromDate = $('#from').val();
            $('#to').attr('min', fromDate);
        });
        // calendar validation
    
        function validateToDate() {
            var today = new Date();
            var dd = String(today.getDate()).padStart(2, '0');
            var mm = String(today.getMonth() + 1).padStart(2, '0');
            var yyyy = today.getFullYear();
    
            today = yyyy + '-' + mm + '-' + dd;
        }
        validateFromDate();
        validateToDate();
    
        // $("#adback").click(function () {
        //     window.location.href = 'ad_profile.html'
        // })
        // $("#edit").click(function () {
        //     window.location.href = 'ad_applyleave.html'
        // })
        // $("#usrback").click(function () {
        //     window.location.href = 'profile.html'
        // })
        // $("#lvrqback").click(function () {
        //     window.location.href = 'ad_leaverequest.html'
        // })
        // $(".icons").click(function () {
        //     alert("leave approoved");
        // })
        // $(".dicons").click(function () {
        //     alert("leave rejected");
        // })
        // // regex password
        // $('#conpswd').click(function (event) {
        //     event.preventDefault();
        //     let pass = $('#newpswd').val();
        //     console.log(pass);
        //     let pwdRegex = (/^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,}$/);
        //     if (!(pass.match(pwdRegex))) {
        //         alert("enter correct form of password");
        //     } else {
        //         alert("enter confirm password");
        //     }
        // })
    
        // // applylv details
        // $('#usrlvbk').hide()
        // $('#adlvbk').hide()
        // $('#dellv').click(function () {
        //     $('table').hide()
        //     $('#dellv').hide()
        //     $('#adcnflv').hide()
        //     $('#cnflv').hide()
        //     $('#usrlvbk').show()
        //     $('#adlvbk').show()
        // })
        // $("#adlvbk").click(function () {
        //     window.location.href = 'ad_applyleave.html'
        // })
        // $("#usrlvbk").click(function () {
        //     window.location.href = 'applyleave.html'
        // })
    
        // $('.leave_status .delete').click(function (event) {
        //     event.preventDefault();
        //     $(this).parent().parent().remove();
        // })
        // $("#profileImage").click(function (e) {
        //     $("#imageUpload").click();
        // });
    
        // $('input[type="file"]').hide();
        // $(".profile-pic").click(function () {
    
        // });
    
        // hide the change photo words
        $("#mySpan").hide();
        $(".profile-pic").hover(function () {
            $("#mySpan").toggle();
        })
    
    
        // employee profile change
        function readURL(input, imgControlName) {
            if (input.files && input.files[0]) {
                var reader = new FileReader();
                reader.onload = function (e) {
                    $(imgControlName).attr('src', e.target.result);
                }
                reader.readAsDataURL(input.files[0]);
            }
        }
        $(".fileToUpload").change(function () {
            var imgControlName = ".ImgPreview";
            readURL(this, imgControlName);
            $('.preview1').addClass('it');
        });
        $(".fileToUpload").change(function () {
            readURL(this);
        });
    // });
    

    // $('#from').on('change', function () {
    //     var fromDate = $('#from').val();
    //     $('#to').attr('min', fromDate);
    // });
    
    // $("#adback").click(function () {
    //     window.location.href = 'ad_profile.html'
    // })
    // $("#edit").click(function () {
    //     window.location.href = 'ad_applyleave.html'
    // })
    // $("#usrback").click(function () {
    //     window.location.href = 'profile.html'
    // })
    // $("#lvrqback").click(function () {
    //     window.location.href = 'ad_leaverequest.html'
    // })
    // $(".icons").click(function () {
    //     alert("leave approoved");
    // })
    // $(".dicons").click(function () {
    //     alert("leave rejected");
    // })
    // // regex password
    // $('#conpswd').click(function (event) {
    //     event.preventDefault();
    //     let pass = $('#newpswd').val();
    //     console.log(pass);
    //     let pwdRegex = (/^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,}$/);
    //     if (!(pass.match(pwdRegex))) {
    //         alert("enter correct form of password");
    //     } else {
    //         alert("enter confirm password");
    //     }
    // })

    // // applylv details
    // $('#usrlvbk').hide()
    // $('#adlvbk').hide()
    // $('#dellv').click(function () {
    //     $('table').hide()
    //     $('#dellv').hide()
    //     $('#adcnflv').hide()
    //     $('#cnflv').hide()
    //     $('#usrlvbk').show()
    //     $('#adlvbk').show()
    // })
    // $("#adlvbk").click(function () {
    //     window.location.href = 'ad_applyleave.html'
    // })
    // $("#usrlvbk").click(function () {
    //     window.location.href = 'applyleave.html'
    // })

    // $('.leave_status .delete').click(function (event) {
    //     event.preventDefault();
    //     $(this).parent().parent().remove();
    // })
    // $("#profileImage").click(function (e) {
    //     $("#imageUpload").click();
    // });

    // $('input[type="file"]').hide();
    // $(".profile-pic").click(function () {

    // });

    // // hide the change photo words
    // $("#mySpan").hide();
    // $(".profile-pic").hover(function () {
    //     $("#mySpan").toggle();
    // })

});
