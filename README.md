# MealGo

**An app to plan meals**

*Story* <br>As a busy adult, I need a way to plan my meals and generate a shopping list to save money and enjoy my favorite foods.

## Screens

**1. LOGIN**

> Signup Dialog

*buttons*
- continue as guest
- sign up

* inform user that the guest mode does not allow synching plans between devices or sharing meals with others.

> Login Dialog

*fields*
- email
- password

*buttons*
- login
- register
- forgot password


**2. MEAL PLAN**
> Month grid with day columns and week rows. Each cell contains all the meals planned for that day. 

> Day detail
- on hover/activate cell
  * plus button to add a meal
  * x button to delete meal
  * edit button to edit meal
- on click plus: go to meal creation screen
- on drag select: allow to add plan

**3. RECIPE**

* Name
* Add ingredients (autocomplete)

**4. SHOPPING**

* For given days, generate list of ingredients needed to complete shopping.

## Architecture

Front end - Vue.js SPA
Back end - Flask API

### Database

Mealgo will use PostgreSQL database for simplicity and ease of development.

#### Entities

**PHASE I**

> **User**
> * email
> * name
> * plans (backref)

> **Plan**
> * name
> * users (backref)
> * meals (backref)

> **UserPlan**
> * user (fk)
> * plan (fk)
> * date_created
> * role (fk)

> **Meal**
> * name
> * plan (fk)
> * date
> * time
> * recipes (backref)

**PHASE II**

> **Recipe**
> * name
> * url (opt)
> * ingredients (opt)
> * meals (backref)

> **MealRecipe**
> * meal (fk)
> * recipe (fk)

> **Ingredient**
> * name
> * recipes (backref)
> * unit (opt)
> * calories (opt)
> * fat (opt)
> * protein (opt)
> * carbs (opt)

> **RecipeIngredient**
> * recipe (fk)
> * ingredient (fk)

**PHASE III**

> **ShoppingList**
> * planner
> * start_date
> * end_date
> * items (backref)
> * date_created
> * date_modified

> **ShopListItem**
> * name
> * unit
> * checked
> * date_added
> * shopping_list (fk)