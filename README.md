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

Front end (container) - Vue.js
Back end (container) - Python / ~~Django API~~ Flask

### Database

Mealgo will use a no-SQL database to aid flexibility and ease horizontal scaling. MongoDB is chosen due to popularity and my personal need to learn it.

#### Entities

> **User**
> * id
> * email

> **Recipe**
> * id
> * name
> * ingredients
>   - { id, order, qty, have }

> **Ingredient**
> * id
> * name

> **Meal**
> * id
> * name
> * recipes
>   - { id, order }

> **WeekPlan**
> * id
> * name?
> * week
> * days
>   - { id }

> **DayPlan**
> * id
> * day
> * meals
>   - { id, order }

> **ShopList**
> * id
> * ingredients
>   - { id, order }