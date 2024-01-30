import uix
from uix.elements import div, button, row
from uix_components import address_form
from uix_components._address_form._address_form import title, description, sample as code

def getformdata(self, id, ctx, data):
    print("Form Data:", data)

def change_lang(ctx, id, value):
    if id == "tur":
        uix.set_lang("tr")
    elif id == "eng":
        uix.set_lang("en")
    ctx.elements["form_example"].update(draw_form)

def draw_form():
    address_form(id="deneme", callback=getformdata)
    
def address_form_example():
    with uix.elements.border().size("fit-content","fit-content").style("overflow-y","auto") as main:
        with row().size("100%","50px").style("gap","10px"):
            button(id="eng", value="English").on("click",change_lang )
            button(id="tur", value="Turkish").on("click",change_lang )
        with row(id="form_example") as form:
            draw_form()
        
    return main