import os

# Define the 41 remaining recipes (excluding Bacon Breakfast Muffins, Berry Oatmeal Bowl, Mini Pancake Bites)
recipes = [
    {
        "name": "Yogurt Parfait",
        "url": "/recipes/yogurt-parfait.html",
        "texture": "Smooth",
        "flavor": "Sweet",
        "continent": "Breakfast Bays",
        "ingredients": ["1 cup yogurt", "1/2 cup granola", "1/2 cup mixed fruit (e.g., berries, banana slices)"],
        "description": "Layered goodness from Breakfast Bays, kid-approved!",
        "instructions": [
            "In a clear glass or bowl, add a layer of yogurt (about 1/3 cup).",
            "Sprinkle a layer of granola (about 2 tbsp) over the yogurt.",
            "Add a layer of mixed fruit (about 2 tbsp).",
            "Repeat layers until all ingredients are used.",
            "Serve immediately or chill for later!"
        ]
    },
    {
        "name": "Banana Yogurt Smoothie",
        "url": "/recipes/banana-yogurt-smoothie.html",
        "texture": "Smooth",
        "flavor": "Sweet",
        "continent": "Breakfast Bays",
        "ingredients": ["1 banana", "1 cup yogurt", "1 tbsp honey"],
        "description": "A creamy smoothie from Breakfast Bays, perfect for picky eaters!",
        "instructions": [
            "Peel and slice the banana.",
            "Add banana, yogurt, and honey to a blender.",
            "Blend until smooth.",
            "Pour into a glass and serve chilled."
        ]
    },
    {
        "name": "Pumpkin Protein Muffins",
        "url": "/recipes/pumpkin-protein-muffins.html",
        "texture": "Soft",
        "flavor": "Sweet",
        "continent": "Breakfast Bays",
        "ingredients": ["1 cup pumpkin puree", "1 cup flour", "1/4 cup protein powder"],
        "description": "Nutritious muffins from Breakfast Bays, great for breakfast!",
        "instructions": [
            "Preheat oven to 350°F (175°C).",
            "Mix pumpkin puree, flour, and protein powder in a bowl.",
            "Pour batter into a greased muffin tin.",
            "Bake for 20 minutes until a toothpick comes out clean.",
            "Cool and serve!"
        ]
    },
    {
        "name": "Air Fryer Sausage Patties",
        "url": "/recipes/air-fryer-sausage-patties.html",
        "texture": "Crisp",
        "flavor": "Mild",
        "continent": "Breakfast Bays",
        "ingredients": ["1 lb ground sausage", "1 tsp spices (e.g., paprika, garlic powder)"],
        "description": "Crispy sausage patties from Breakfast Bays, kid-friendly!",
        "instructions": [
            "Mix ground sausage with spices.",
            "Form into small patties.",
            "Place in air fryer at 400°F for 8-10 minutes, flipping halfway.",
            "Serve warm with eggs or toast."
        ]
    },
    {
        "name": "French Toast Sticks",
        "url": "/recipes/french-toast-sticks.html",
        "texture": "Crisp",
        "flavor": "Sweet",
        "continent": "Breakfast Bays",
        "ingredients": ["4 slices bread", "2 eggs", "1 tsp cinnamon"],
        "description": "Dippable toast sticks from Breakfast Bays, fun for kids!",
        "instructions": [
            "Cut bread into strips.",
            "Whisk eggs and cinnamon in a bowl.",
            "Dip bread strips in egg mixture.",
            "Cook on a greased skillet over medium heat until golden, about 2 minutes per side.",
            "Serve with syrup or fruit."
        ]
    },
    {
        "name": "Cheesy Egg Muffins",
        "url": "/recipes/cheesy-egg-muffins.html",
        "texture": "Soft",
        "flavor": "Mild",
        "continent": "Breakfast Bays",
        "ingredients": ["4 eggs", "1/2 cup cheese", "1/4 cup milk"],
        "description": "Fluffy egg muffins from Breakfast Bays, perfect for breakfast!",
        "instructions": [
            "Preheat oven to 350°F (175°C).",
            "Whisk eggs, cheese, and milk in a bowl.",
            "Pour into a greased muffin tin.",
            "Bake for 15-20 minutes until set.",
            "Serve warm."
        ]
    },
    {
        "name": "Apple Cinnamon Oatmeal",
        "url": "/recipes/apple-cinnamon-oatmeal.html",
        "texture": "Smooth",
        "flavor": "Sweet",
        "continent": "Breakfast Bays",
        "ingredients": ["1 cup oats", "1 apple, diced", "1 tsp cinnamon"],
        "description": "Warm oatmeal from Breakfast Bays, kid-approved!",
        "instructions": [
            "Cook oats in 2 cups water over medium heat for 5 minutes.",
            "Add diced apple and cinnamon.",
            "Stir and cook for 2-3 more minutes.",
            "Serve warm with a splash of milk."
        ]
    },
    {
        "name": "Peanut Butter Toast",
        "url": "/recipes/peanut-butter-toast.html",
        "texture": "Crisp",
        "flavor": "Sweet",
        "continent": "Breakfast Bays",
        "ingredients": ["2 slices bread", "2 tbsp peanut butter", "1 tbsp honey"],
        "description": "Simple toast from Breakfast Bays, a picky eater favorite!",
        "instructions": [
            "Toast bread until golden.",
            "Spread peanut butter on warm toast.",
            "Drizzle with honey.",
            "Serve immediately."
        ]
    },
    {
        "name": "Blueberry Waffles",
        "url": "/recipes/blueberry-waffles.html",
        "texture": "Crisp",
        "flavor": "Sweet",
        "continent": "Breakfast Bays",
        "ingredients": ["1 cup flour", "1/2 cup blueberries", "1 cup milk"],
        "description": "Crispy waffles from Breakfast Bays, bursting with blueberries!",
        "instructions": [
            "Mix flour, milk, and blueberries to make a batter.",
            "Preheat a waffle iron and grease lightly.",
            "Pour batter into the waffle iron.",
            "Cook until golden, about 5-7 minutes.",
            "Serve with syrup or whipped cream."
        ]
    },
    {
        "name": "Cheesy Veggie Tots",
        "url": "/recipes/cheesy-veggie-tots.html",
        "texture": "Crunchy",
        "flavor": "Mild",
        "continent": "Lunch Lands",
        "ingredients": ["2 cups potatoes, shredded", "1/2 cup cheese", "1/2 cup zucchini, shredded"],
        "description": "Crispy tots from Lunch Lands, packed with veggies!",
        "instructions": [
            "Preheat oven to 400°F (200°C).",
            "Mix shredded potatoes, cheese, and zucchini.",
            "Form into small tots and place on a baking sheet.",
            "Bake for 20-25 minutes until crispy.",
            "Serve with ketchup."
        ]
    },
    {
        "name": "Chicken Salad Sandwich",
        "url": "/recipes/chicken-salad-sandwich.html",
        "texture": "Smooth",
        "flavor": "Mild",
        "continent": "Lunch Lands",
        "ingredients": ["1 cup cooked chicken, shredded", "2 tbsp mayonnaise", "2 slices bread"],
        "description": "Creamy sandwich from Lunch Lands, perfect for kids!",
        "instructions": [
            "Mix shredded chicken with mayonnaise.",
            "Spread mixture on one slice of bread.",
            "Top with another slice.",
            "Cut into triangles and serve."
        ]
    },
    {
        "name": "Turkey Roll Ups",
        "url": "/recipes/turkey-roll-ups.html",
        "texture": "Soft",
        "flavor": "Mild",
        "continent": "Lunch Lands",
        "ingredients": ["4 slices turkey", "1 tortilla", "1/4 cup cheese"],
        "description": "Fun roll-ups from Lunch Lands, great for lunchboxes!",
        "instructions": [
            "Lay tortilla flat and sprinkle with cheese.",
            "Add turkey slices evenly.",
            "Roll up tightly and slice into rounds.",
            "Serve with a dipping sauce."
        ]
    },
    {
        "name": "Mini Chicken Burgers",
        "url": "/recipes/mini-chicken-burgers.html",
        "texture": "Crisp",
        "flavor": "Mild",
        "continent": "Lunch Lands",
        "ingredients": ["1/2 lb ground chicken", "1/4 cup breadcrumbs", "4 mini buns"],
        "description": "Tiny burgers from Lunch Lands, kid-sized fun!",
        "instructions": [
            "Mix ground chicken with breadcrumbs and form into small patties.",
            "Cook patties in a skillet over medium heat for 4-5 minutes per side.",
            "Place patties in mini buns.",
            "Serve with ketchup or mayo."
        ]
    },
    {
        "name": "Pesto Chicken Bake",
        "url": "/recipes/pesto-chicken-bake.html",
        "texture": "Soft",
        "flavor": "Mild",
        "continent": "Lunch Lands",
        "ingredients": ["2 chicken breasts", "2 tbsp pesto", "1/2 cup mozzarella"],
        "description": "Flavorful bake from Lunch Lands, easy and cheesy!",
        "instructions": [
            "Preheat oven to 375°F (190°C).",
            "Spread pesto over chicken breasts.",
            "Top with mozzarella and place in a baking dish.",
            "Bake for 25-30 minutes until chicken is cooked.",
            "Serve warm."
        ]
    },
    {
        "name": "Cheeseburger Biscuits",
        "url": "/recipes/cheeseburger-biscuits.html",
        "texture": "Crisp",
        "flavor": "Mild",
        "continent": "Lunch Lands",
        "ingredients": ["1/2 lb ground beef", "1/2 cup cheese", "1 can biscuit dough"],
        "description": "Burger-inspired biscuits from Lunch Lands, fun for kids!",
        "instructions": [
            "Preheat oven to 375°F (190°C).",
            "Cook ground beef until browned, then mix with cheese.",
            "Flatten biscuit dough and fill with beef mixture.",
            "Fold and bake for 12-15 minutes until golden.",
            "Serve warm."
        ]
    },
    {
        "name": "Veggie Wraps",
        "url": "/recipes/veggie-wraps.html",
        "texture": "Soft",
        "flavor": "Mild",
        "continent": "Lunch Lands",
        "ingredients": ["1 tortilla", "1/2 cup lettuce", "1/4 cup cheese"],
        "description": "Fresh wraps from Lunch Lands, perfect for picky eaters!",
        "instructions": [
            "Lay tortilla flat and add lettuce and cheese.",
            "Roll up tightly.",
            "Slice into rounds and serve."
        ]
    },
    {
        "name": "Ham and Cheese Sliders",
        "url": "/recipes/ham-and-cheese-sliders.html",
        "texture": "Soft",
        "flavor": "Mild",
        "continent": "Lunch Lands",
        "ingredients": ["4 slices ham", "4 slices cheese", "4 slider rolls"],
        "description": "Mini sliders from Lunch Lands, kid-friendly and easy!",
        "instructions": [
            "Preheat oven to 350°F (175°C).",
            "Place ham and cheese inside slider rolls.",
            "Arrange in a baking dish and cover with foil.",
            "Bake for 10-12 minutes until cheese melts.",
            "Serve warm."
        ]
    },
    {
        "name": "Peanut Butter Banana Sandwich",
        "url": "/recipes/peanut-butter-banana-sandwich.html",
        "texture": "Smooth",
        "flavor": "Sweet",
        "continent": "Lunch Lands",
        "ingredients": ["2 tbsp peanut butter", "1 banana, sliced", "2 slices bread"],
        "description": "Sweet sandwich from Lunch Lands, a kid favorite!",
        "instructions": [
            "Spread peanut butter on one slice of bread.",
            "Add banana slices and top with another slice.",
            "Cut into triangles and serve."
        ]
    },
    {
        "name": "Mac and Cheese Cups",
        "url": "/recipes/mac-and-cheese-cups.html",
        "texture": "Soft",
        "flavor": "Mild",
        "continent": "Lunch Lands",
        "ingredients": ["1 cup pasta", "1/2 cup cheese", "1/4 cup milk"],
        "description": "Cheesy cups from Lunch Lands, perfect for kids!",
        "instructions": [
            "Cook pasta according to package instructions.",
            "Mix cooked pasta with cheese and milk in a saucepan until melted.",
            "Spoon into a greased muffin tin.",
            "Bake at 350°F (175°C) for 15 minutes.",
            "Serve warm."
        ]
    },
    {
        "name": "Tuna Melt Bites",
        "url": "/recipes/tuna-melt-bites.html",
        "texture": "Crisp",
        "flavor": "Mild",
        "continent": "Lunch Lands",
        "ingredients": ["1 can tuna", "1/4 cup cheese", "4 slices bread"],
        "description": "Crispy bites from Lunch Lands, great for lunch!",
        "instructions": [
            "Mix tuna with cheese.",
            "Spread on bread slices and cut into small squares.",
            "Bake at 375°F (190°C) for 10-12 minutes until crispy.",
            "Serve warm."
        ]
    },
    {
        "name": "Pizza Roll Ups",
        "url": "/recipes/pizza-roll-ups.html",
        "texture": "Crisp",
        "flavor": "Mild",
        "continent": "Lunch Lands",
        "ingredients": ["1 tortilla", "1/4 cup pizza sauce", "1/2 cup cheese"],
        "description": "Pizza-inspired roll-ups from Lunch Lands, kid-approved!",
        "instructions": [
            "Spread pizza sauce on tortilla and sprinkle with cheese.",
            "Roll up tightly and slice into rounds.",
            "Bake at 375°F (190°C) for 8-10 minutes.",
            "Serve with extra sauce."
        ]
    },
    {
        "name": "Mini Cheese Quesadillas",
        "url": "/recipes/mini-cheese-quesadillas.html",
        "texture": "Crisp",
        "flavor": "Mild",
        "continent": "Dinner Dell",
        "ingredients": ["4 small tortillas", "1/2 cup cheese", "1 tbsp butter"],
        "description": "Crispy quesadillas from Dinner Dell, perfect for kids!",
        "instructions": [
            "Spread cheese on one tortilla and top with another.",
            "Melt butter in a skillet over medium heat.",
            "Cook quesadilla for 2-3 minutes per side until golden.",
            "Cut into wedges and serve."
        ]
    },
    {
        "name": "Baked Spaghetti",
        "url": "/recipes/baked-spaghetti.html",
        "texture": "Soft",
        "flavor": "Mild",
        "continent": "Dinner Dell",
        "ingredients": ["1/2 lb spaghetti", "1 cup tomato sauce", "1/2 cup cheese"],
        "description": "Cheesy spaghetti from Dinner Dell, a family favorite!",
        "instructions": [
            "Cook spaghetti according to package instructions.",
            "Mix with tomato sauce and place in a baking dish.",
            "Top with cheese and bake at 350°F (175°C) for 20 minutes.",
            "Serve warm."
        ]
    },
    {
        "name": "Chicken Nuggets",
        "url": "/recipes/chicken-nuggets.html",
        "texture": "Crunchy",
        "flavor": "Mild",
        "continent": "Dinner Dell",
        "ingredients": ["1/2 lb chicken breast, cubed", "1/2 cup breadcrumbs", "1 egg"],
        "description": "Crispy nuggets from Dinner Dell, kid-friendly!",
        "instructions": [
            "Preheat oven to 400°F (200°C).",
            "Dip chicken cubes in beaten egg, then coat with breadcrumbs.",
            "Place on a baking sheet and bake for 15-20 minutes.",
            "Serve with ketchup."
        ]
    },
    {
        "name": "Tater Tot Casserole",
        "url": "/recipes/tater-tot-casserole.html",
        "texture": "Crisp",
        "flavor": "Mild",
        "continent": "Dinner Dell",
        "ingredients": ["2 cups tater tots", "1/2 lb ground beef", "1/2 cup cheese"],
        "description": "Crispy casserole from Dinner Dell, a kid favorite!",
        "instructions": [
            "Preheat oven to 375°F (190°C).",
            "Cook ground beef until browned and place in a baking dish.",
            "Top with cheese and tater tots.",
            "Bake for 25-30 minutes until golden.",
            "Serve warm."
        ]
    },
    {
        "name": "Slow Cooker Chicken Tacos",
        "url": "/recipes/slow-cooker-chicken-tacos.html",
        "texture": "Soft",
        "flavor": "Mild",
        "continent": "Dinner Dell",
        "ingredients": ["1 lb chicken breast", "1 tbsp taco seasoning", "4 tortillas"],
        "description": "Tender tacos from Dinner Dell, easy and delicious!",
        "instructions": [
            "Place chicken and taco seasoning in a slow cooker.",
            "Cook on low for 6-8 hours or high for 3-4 hours.",
            "Shred chicken and serve in tortillas.",
            "Top with cheese or salsa."
        ]
    },
    {
        "name": "Cheeseburger Hot Dish",
        "url": "/recipes/cheeseburger-hot-dish.html",
        "texture": "Crisp",
        "flavor": "Mild",
        "continent": "Dinner Dell",
        "ingredients": ["1/2 lb ground beef", "2 cups tater tots", "1/2 cup cheese"],
        "description": "Hearty hot dish from Dinner Dell, kid-approved!",
        "instructions": [
            "Preheat oven to 375°F (190°C).",
            "Cook ground beef until browned and place in a baking dish.",
            "Top with cheese and tater tots.",
            "Bake for 25-30 minutes until crispy.",
            "Serve warm."
        ]
    },
    {
        "name": "Chicken Parmesan Meatballs",
        "url": "/recipes/chicken-parmesan-meatballs.html",
        "texture": "Soft",
        "flavor": "Mild",
        "continent": "Dinner Dell",
        "ingredients": ["1/2 lb ground chicken", "1/4 cup breadcrumbs", "1/2 cup cheese"],
        "description": "Cheesy meatballs from Dinner Dell, perfect for kids!",
        "instructions": [
            "Preheat oven to 375°F (190°C).",
            "Mix ground chicken, breadcrumbs, and cheese.",
            "Form into meatballs and place on a baking sheet.",
            "Bake for 20-25 minutes until cooked.",
            "Serve with sauce."
        ]
    },
    {
        "name": "Ground Beef Noodle Casserole",
        "url": "/recipes/ground-beef-noodle-casserole.html",
        "texture": "Soft",
        "flavor": "Mild",
        "continent": "Dinner Dell",
        "ingredients": ["1/2 lb pasta", "1/2 lb ground beef", "1/2 cup cheese"],
        "description": "Comforting casserole from Dinner Dell, a family hit!",
        "instructions": [
            "Cook pasta according to package instructions.",
            "Cook ground beef until browned.",
            "Mix pasta, beef, and cheese in a baking dish.",
            "Bake at 350°F (175°C) for 20 minutes.",
            "Serve warm."
        ]
    },
    {
        "name": "Chicken Alfredo",
        "url": "/recipes/chicken-alfredo.html",
        "texture": "Smooth",
        "flavor": "Mild",
        "continent": "Dinner Dell",
        "ingredients": ["1/2 lb chicken breast", "1/2 lb pasta", "1 cup alfredo sauce"],
        "description": "Creamy alfredo from Dinner Dell, kid-friendly!",
        "instructions": [
            "Cook pasta according to package instructions.",
            "Cook chicken until done and slice.",
            "Mix pasta, chicken, and alfredo sauce in a pan.",
            "Heat through and serve."
        ]
    },
    {
        "name": "French Bread Pizza",
        "url": "/recipes/french-bread-pizza.html",
        "texture": "Crisp",
        "flavor": "Mild",
        "continent": "Dinner Dell",
        "ingredients": ["1 loaf French bread", "1/2 cup pizza sauce", "1 cup cheese"],
        "description": "Easy pizza from Dinner Dell, perfect for kids!",
        "instructions": [
            "Preheat oven to 400°F (200°C).",
            "Slice French bread in half and spread with pizza sauce.",
            "Top with cheese.",
            "Bake for 10-12 minutes until cheese is melted.",
            "Serve warm."
        ]
    },
    {
        "name": "Sesame Chicken Meatballs",
        "url": "/recipes/sesame-chicken-meatballs.html",
        "texture": "Soft",
        "flavor": "Sweet",
        "continent": "Dinner Dell",
        "ingredients": ["1/2 lb ground chicken", "2 tbsp honey", "1 tsp ginger"],
        "description": "Sweet meatballs from Dinner Dell, a kid favorite!",
        "instructions": [
            "Preheat oven to 375°F (190°C).",
            "Mix ground chicken, honey, and ginger.",
            "Form into meatballs and place on a baking sheet.",
            "Bake for 20-25 minutes until cooked.",
            "Serve with rice."
        ]
    },
    {
        "name": "Chili Dog Casserole",
        "url": "/recipes/chili-dog-casserole.html",
        "texture": "Crisp",
        "flavor": "Mild",
        "continent": "Dinner Dell",
        "ingredients": ["4 hot dogs", "1 cup cornbread mix", "1/2 cup cheese"],
        "description": "Fun casserole from Dinner Dell, great for kids!",
        "instructions": [
            "Preheat oven to 375°F (190°C).",
            "Slice hot dogs and place in a baking dish.",
            "Prepare cornbread mix and pour over hot dogs.",
            "Top with cheese and bake for 20-25 minutes.",
            "Serve warm."
        ]
    },
    {
        "name": "Strawberry Cream Pops",
        "url": "/recipes/strawberry-cream-pops.html",
        "texture": "Smooth",
        "flavor": "Sweet",
        "continent": "Dessert Dunes",
        "ingredients": ["1 cup strawberries", "1 cup yogurt", "2 tbsp honey"],
        "description": "Cool pops from Dessert Dunes, perfect for kids!",
        "instructions": [
            "Blend strawberries, yogurt, and honey until smooth.",
            "Pour into popsicle molds.",
            "Freeze for 4-6 hours.",
            "Serve chilled."
        ]
    },
    {
        "name": "Homemade Dunkaroos",
        "url": "/recipes/homemade-dunkaroos.html",
        "texture": "Crisp",
        "flavor": "Sweet",
        "continent": "Dessert Dunes",
        "ingredients": ["1 cup shortbread cookies", "1/2 cup frosting", "2 tbsp sprinkles"],
        "description": "Fun dippers from Dessert Dunes, a kid favorite!",
        "instructions": [
            "Arrange shortbread cookies on a plate.",
            "Mix frosting with sprinkles.",
            "Serve cookies with frosting for dipping."
        ]
    },
    {
        "name": "Rainbow Fruit Skewers",
        "url": "/recipes/rainbow-fruit-skewers.html",
        "texture": "Crisp",
        "flavor": "Sweet",
        "continent": "Dessert Dunes",
        "ingredients": ["1 cup strawberries", "1/2 cup pineapple", "1/2 cup grapes"],
        "description": "Colorful skewers from Dessert Dunes, fun for kids!",
        "instructions": [
            "Cut fruit into bite-sized pieces.",
            "Thread fruit onto skewers in a rainbow pattern.",
            "Serve fresh."
        ]
    },
    {
        "name": "Chocolate Banana Bites",
        "url": "/recipes/chocolate-banana-bites.html",
        "texture": "Smooth",
        "flavor": "Sweet",
        "continent": "Dessert Dunes",
        "ingredients": ["1 banana", "1/2 cup chocolate, melted", "2 tbsp peanuts, crushed"],
        "description": "Sweet bites from Dessert Dunes, perfect for picky eaters!",
        "instructions": [
            "Slice banana into rounds.",
            "Dip each round in melted chocolate.",
            "Sprinkle with crushed peanuts.",
            "Chill in the fridge for 10 minutes.",
            "Serve cold."
        ]
    },
    {
        "name": "Peanut Butter Cookies",
        "url": "/recipes/peanut-butter-cookies.html",
        "texture": "Crisp",
        "flavor": "Sweet",
        "continent": "Dessert Dunes",
        "ingredients": ["1/2 cup peanut butter", "1/4 cup sugar", "1/2 cup flour"],
        "description": "Crispy cookies from Dessert Dunes, a kid classic!",
        "instructions": [
            "Preheat oven to 350°F (175°C).",
            "Mix peanut butter, sugar, and flour.",
            "Roll into balls and place on a baking sheet.",
            "Flatten with a fork and bake for 10-12 minutes.",
            "Cool and serve."
        ]
    },
    {
        "name": "Apple Pie Bites",
        "url": "/recipes/apple-pie-bites.html",
        "texture": "Crisp",
        "flavor": "Sweet",
        "continent": "Dessert Dunes",
        "ingredients": ["1 apple, diced", "1 tsp cinnamon", "1 sheet pastry"],
        "description": "Mini pies from Dessert Dunes, kid-friendly!",
        "instructions": [
            "Preheat oven to 375°F (190°C).",
            "Mix diced apple with cinnamon.",
            "Cut pastry into squares and fill with apple mixture.",
            "Fold and bake for 15-20 minutes until golden.",
            "Serve warm."
        ]
    },
    {
        "name": "Yogurt Fruit Pops",
        "url": "/recipes/yogurt-fruit-pops.html",
        "texture": "Smooth",
        "flavor": "Sweet",
        "continent": "Dessert Dunes",
        "ingredients": ["1 cup yogurt", "1/2 cup berries", "2 tbsp honey"],
        "description": "Cool pops from Dessert Dunes, great for kids!",
        "instructions": [
            "Blend yogurt, berries, and honey until smooth.",
            "Pour into popsicle molds.",
            "Freeze for 4-6 hours.",
            "Serve chilled."
        ]
    },
    {
        "name": "Oatmeal Raisin Bars",
        "url": "/recipes/oatmeal-raisin-bars.html",
        "texture": "Soft",
        "flavor": "Sweet",
        "continent": "Dessert Dunes",
        "ingredients": ["1 cup oats", "1/2 cup raisins", "1/4 cup brown sugar"],
        "description": "Chewy bars from Dessert Dunes, perfect for snacks!",
        "instructions": [
            "Preheat oven to 350°F (175°C).",
            "Mix oats, raisins, and brown sugar.",
            "Press into a greased baking dish.",
            "Bake for 20-25 minutes until set.",
            "Cut into bars and serve."
        ]
    }
]

# HTML template for recipe pages
html_template = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{name} - {continent} Recipe</title>
  <meta name="description" content="{description} at Little Chefs Big Adventures. Perfect for picky eaters!">
  <meta name="keywords" content="picky eater recipes, kid-friendly recipes, {name_lower}, Nibbletopia">
  <link rel="stylesheet" href="../styles.css">
  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@type": "Recipe",
    "name": "{name}",
    "description": "{description}",
    "recipeIngredient": {ingredients},
    "recipeInstructions": {instructions}
  }}
  </script>
</head>
<body>
  <header>
    <h1>Little Chefs Big Adventures</h1>
    <nav>
      <ul>
        <li><a href="../index.html">Home</a></li>
        <li><a href="../recipe-finder.html">Recipe Finder</a></li>
        <li><a href="../recipes.html">Recipes</a></li>
        <li><a href="../subscribe.html">Subscribe</a></li>
      </ul>
    </nav>
  </header>
  <main>
    <h2>{name}</h2>
    <p>{description}</p>
    <h3>Ingredients</h3>
    <ul>
{ingredients_html}
    </ul>
    <h3>Instructions</h3>
    <ol>
{instructions_html}
    </ol>
    <p><a href="../recipe-finder.html">Back to Recipe Finder</a> | <a href="../subscribe.html">Join Our Newsletter</a></p>
  </main>
  <footer>
    <p>Join our newsletter for more picky eater tips!</p>
    <form action="https://static.mailerlite.com/webforms/submit/XXXXX" method="post" target="_blank">
      <label for="email">Email:</label>
      <input type="email" name="fields[email]" id="email" placeholder="Enter your email" required>
      <button type="submit">Subscribe</button>
    </form>
  </footer>
</body>
</html>
"""

# Create recipes folder if it doesn't exist
if not os.path.exists("recipes"):
    os.makedirs("recipes")

# Generate HTML files for each recipe
for recipe in recipes:
    name = recipe["name"]
    name_lower = name.lower().replace(" ", "-")
    description = recipe["description"]
    ingredients = recipe["ingredients"]
    instructions = recipe["instructions"]
    continent = recipe["continent"]
    
    # Format ingredients and instructions for HTML and JSON-LD
    ingredients_html = "\n".join(f"      <li>{ing}</li>" for ing in ingredients)
    instructions_html = "\n".join(f"      <li>{inst}</li>" for inst in instructions)
    ingredients_json = str(ingredients)
    instructions_json = str([{"@type": "HowToStep", "text": inst} for inst in instructions])
    
    # Fill the HTML template
    html_content = html_template.format(
        name=name,
        name_lower=name_lower,
        description=description,
        ingredients=ingredients_json,
        instructions=instructions_json,
        ingredients_html=ingredients_html,
        instructions_html=instructions_html,
        continent=continent
    )
    
    # Save the HTML file
    filename = f"recipes/{name_lower}.html"
    with open(filename, "w") as f:
        f.write(html_content)
    print(f"Generated {filename}")

print("All recipe HTML files have been generated in the 'recipes' folder.")
