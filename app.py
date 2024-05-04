"""Pet Adoption Agency"""

from flask import Flask, render_template, redirect, flash
from flask_debugtoolbar import DebugToolbarExtension
from models import connect_db, db, Pet
from forms import AddPetForm, EditPetForm

app = Flask(__name__)
app.app_context().push()

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///adoption_agency'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

app.config['SECRET_KEY'] = "I wish I had a puppy or two"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

debug = DebugToolbarExtension(app)

connect_db(app)
db.create_all()

@app.route("/")
def home_page():
    """Redirects to list of pets"""
    
    return redirect("/pets")

@app.route("/pets")
def list_pets():
    """Show list of pets"""
    
    pets = db.session.query(Pet.id, Pet.name, Pet.photo_url, Pet.available).all()
    
    return render_template("pets_list.html", pets = pets)

@app.route("/add_pet", methods=["GET", "POST"])
def add_pet():
    """Adds a Pet"""

    form = AddPetForm()
    
    if form.validate_on_submit():
        pet_data = {
            "name": form.name.data,
            "species": form.species.data,
            "photo_url": form.photo_url.data or Pet.photo_url.default.arg,
            "age": form.age.data,
            "notes": form.notes.data
        }
           
        new_pet = Pet(**pet_data)
     
        db.session.add(new_pet)
        db.session.commit()
        
        name = pet_data["name"]
        species = pet_data["species"]        
        flash(f"Added new pet! {name} the {species}!")
        
        return redirect("/")

    else:
        return render_template("pet_add_form.html", form=form)
    
@app.route("/pets/<pet_id>", methods=["GET", "POST"])
def show_pet_details(pet_id):
    """Show pet details"""
    
    pet = Pet.query.get_or_404(pet_id)
    
    form = EditPetForm(obj=pet)
    
    if form.validate_on_submit():
        pet_data = {
            "name": form.name.data,
            "photo_url": form.photo_url.data,
            "notes": form.notes.data,
            "available": form.available.data
        }
        
        pet.name = pet_data.get("name")
        pet.photo_url = pet_data.get("photo_url") or Pet.photo_url.default.arg
        pet.notes = pet_data.get("notes")
        pet.available = pet_data.get("available")
           
        db.session.add(pet)
        db.session.commit()
               
        flash(f"Edited {pet.name} the {pet.species}!")
        
        return redirect(f"/pets/{pet_id}")

    else:
        return render_template("pet_details.html", form=form, pet=pet)
