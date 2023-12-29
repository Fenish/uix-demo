from uix.elements import input, button, border, div, col, form, row

def input_example():
    input("", placeholder="Kullanıcı Adı", required=True)
    input("",type="password", placeholder="Şifre")
    input("",type="number", placeholder="Sayı")
    input("2024-01-01T00:00",type="datetime-local", placeholder="Tarih ve Saat")
    input("",type="date")
    input("",type="time")
    
    def on_change(ctx, id, value):
        if value!= "":
            ctx.elements["submitButton"].attrs.pop("disabled", None)
            ctx.elements["submitButton"].update()
            
        else:
            ctx.elements["submitButton"].attrs["disabled"] = True
            ctx.elements["submitButton"].update()
            
           

    with border("").style("padding","20px").style("width","50%"):
        input(id="userName", placeholder="Kullanıcı Adı", required=True).on("input",on_change)
        with row("").style("display","flex").style("justify-content","space-between"):
            div("Zorunlu alanlar doldurulmalıdır.").style("font-size","10px")
            button("Gönder", id="submitButton", type="submit", disabled = True)



    