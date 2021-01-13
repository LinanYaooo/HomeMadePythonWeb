;
var member_reg_ops = {
        init: function () {
            this.eventBind();
        },
        eventBind: function () {
            $(".do-reg").click(
                function () {
                    alert(1);
                    console.log(123);
                }
            );
        }
    }
;