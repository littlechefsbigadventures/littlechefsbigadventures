const recipes = [
  {
    name: "Bacon Breakfast Muffins",
    url: "/recipes/bacon-breakfast-muffins.html",
    texture: "Crisp",
    flavor: "Mild",
    continent: "Breakfast Bays",
    ingredients: ["bacon", "eggs", "cheese"]
  },
  {
    name: "Berry Oatmeal Bowl",
    url: "/recipes/berry-oatmeal-bowl.html",
    texture: "Smooth",
    flavor: "Sweet",
    continent: "Breakfast Bays",
    ingredients: ["oats", "berries", "milk"]
  },
  {
    name: "Mini Pancake Bites",
    url: "/recipes/mini-pancake-bites.html",
    texture: "Soft",
    flavor: "Sweet",
    continent: "Breakfast Bays",
    ingredients: ["flour", "milk", "sugar"]
  },
  {
    name: "Banana Yogurt Smoothie",
    url: "/recipes/banana-yogurt-smoothie.html",
    texture: "Smooth",
    flavor: "Sweet",
    continent: "Breakfast Bays",
    ingredients: ["banana", "yogurt", "honey"]
  },
  {
    name: "Pumpkin Protein Muffins",
    url: "/recipes/pumpkin-protein-muffins.html",
    texture: "Soft",
    flavor: "Sweet",
    continent: "Breakfast Bays",
    ingredients: ["pumpkin puree", "flour", "protein powder"]
  },
  {
    name: "Air Fryer Sausage Patties",
    url: "/recipes/air-fryer-sausage-patties.html",
    texture: "Crisp",
    flavor: "Mild",
    continent: "Breakfast Bays",
    ingredients: ["ground sausage", "spices"]
  },
  {
    name: "Yogurt Parfait",
    url: "/recipes/yogurt-parfait.html",
    texture: "Smooth",
    flavor: "Sweet",
    continent: "Breakfast Bays",
    ingredients: ["yogurt", "granola", "fruit"]
  },
  {
    name: "French Toast Sticks",
    url: "/recipes/french-toast-sticks.html",
    texture: "Crisp",
    flavor: "Sweet",
    continent: "Breakfast Bays",
    ingredients: ["bread", "eggs", "cinnamon"]
  },
  {
    name: "Cheesy Egg Muffins",
    url: "/recipes/cheesy-egg-muffins.html",
    texture: "Soft",
    flavor: "Mild",
    continent: "Breakfast Bays",
    ingredients: ["eggs", "cheese", "milk"]
  },
  {
    name: "Apple Cinnamon Oatmeal",
    url: "/recipes/apple-cinnamon-oatmeal.html",
    texture: "Smooth",
    flavor: "Sweet",
    continent: "Breakfast Bays",
    ingredients: ["oats", "apple", "cinnamon"]
  },
  {
    name: "Peanut Butter Toast",
    url: "/recipes/peanut-butter-toast.html",
    texture: "Crisp",
    flavor: "Sweet",
    continent: "Breakfast Bays",
    ingredients: ["bread", "peanut butter", "honey"]
  },
  {
    name: "Blueberry Waffles",
    url: "/recipes/blueberry-waffles.html",
    texture: "Crisp",
    flavor: "Sweet",
    continent: "Breakfast Bays",
    ingredients: ["flour", "blueberries", "milk"]
  },
  {
    name: "Cheesy Veggie Tots",
    url: "/recipes/cheesy-veggie-tots.html",
    texture: "Crunchy",
    flavor: "Mild",
    continent: "Lunch Lands",
    ingredients: ["potatoes", "cheese", "zucchini"]
  },
  {
    name: "Chicken Salad Sandwich",
    url: "/recipes/chicken-salad-sandwich.html",
    texture: "Smooth",
    flavor: "Mild",
    continent: "Lunch Lands",
    ingredients: ["chicken", "mayonnaise", "bread"]
  },
  {
    name: "Turkey Roll Ups",
    url: "/recipes/turkey-roll-ups.html",
    texture: "Soft",
    flavor: "Mild",
    continent: "Lunch Lands",
    ingredients: ["turkey", "tortilla", "cheese"]
  },
  {
    name: "Mini Chicken Burgers",
    url: "/recipes/mini-chicken-burgers.html",
    texture: "Crisp",
    flavor: "Mild",
    continent: "Lunch Lands",
    ingredients: ["ground chicken", "breadcrumbs", "buns"]
  },
  {
    name: "Pesto Chicken Bake",
    url: "/recipes/pesto-chicken-bake.html",
    texture: "Soft",
    flavor: "Mild",
    continent: "Lunch Lands",
    ingredients: ["chicken", "pesto", "mozzarella"]
  },
  {
    name: "Cheeseburger Biscuits",
    url: "/recipes/cheeseburger-biscuits.html",
    texture: "Crisp",
    flavor: "Mild",
    continent: "Lunch Lands",
    ingredients: ["ground beef", "cheese", "biscuit dough"]
  },
  {
    name: "Veggie Wraps",
    url: "/recipes/veggie-wraps.html",
    texture: "Soft",
    flavor: "Mild",
    continent: "Lunch Lands",
    ingredients: ["tortilla", "lettuce", "cheese"]
  },
  {
    name: "Ham and Cheese Sliders",
    url: "/recipes/ham-and-cheese-sliders.html",
    texture: "Soft",
    flavor: "Mild",
    continent: "Lunch Lands",
    ingredients: ["ham", "cheese", "rolls"]
  },
  {
    name: "Peanut Butter Banana Sandwich",
    url: "/recipes/peanut-butter-banana-sandwich.html",
    texture: "Smooth",
    flavor: "Sweet",
    continent: "Lunch Lands",
    ingredients: ["peanut butter", "banana", "bread"]
  },
  {
    name: "Mac and Cheese Cups",
    url: "/recipes/mac-and-cheese-cups.html",
    texture: "Soft",
    flavor: "Mild",
    continent: "Lunch Lands",
    ingredients: ["pasta", "cheese", "milk"]
  },
  {
    name: "Tuna Melt Bites",
    url: "/recipes/tuna-melt-bites.html",
    texture: "Crisp",
    flavor: "Mild",
    continent: "Lunch Lands",
    ingredients: ["tuna", "cheese", "bread"]
  },
  {
    name: "Pizza Roll Ups",
    url: "/recipes/pizza-roll-ups.html",
    texture: "Crisp",
    flavor: "Mild",
    continent: "Lunch Lands",
    ingredients: ["tortilla", "pizza sauce", "cheese"]
  },
  {
    name: "Mini Cheese Quesadillas",
    url: "/recipes/mini-cheese-quesadillas.html",
    texture: "Crisp",
    flavor: "Mild",
    continent: "Dinner Dell",
    ingredients: ["tortillas", "cheese", "butter"]
  },
  {
    name: "Baked Spaghetti",
    url: "/recipes/baked-spaghetti.html",
    texture: "Soft",
    flavor: "Mild",
    continent: "Dinner Dell",
    ingredients: ["spaghetti", "tomato sauce", "cheese"]
  },
  {
    name: "Chicken Nuggets",
    url: "/recipes/chicken-nuggets.html",
    texture: "Crunchy",
    flavor: "Mild",
    continent: "Dinner Dell",
    ingredients: ["chicken", "breadcrumbs", "egg"]
  },
  {
    name: "Tater Tot Casserole",
    url: "/recipes/tater-tot-casserole.html",
    texture: "Crisp",
    flavor: "Mild",
    continent: "Dinner Dell",
    ingredients: ["tater tots", "ground beef", "cheese"]
  },
  {
    name: "Slow Cooker Chicken Tacos",
    url: "/recipes/slow-cooker-chicken-tacos.html",
    texture: "Soft",
    flavor: "Mild",
    continent: "Dinner Dell",
    ingredients: ["chicken", "taco seasoning", "tortillas"]
  },
  {
    name: "Cheeseburger Hot Dish",
    url: "/recipes/cheeseburger-hot-dish.html",
    texture: "Crisp",
    flavor: "Mild",
    continent: "Dinner Dell",
    ingredients: ["ground beef", "tater tots", "cheese"]
  },
  {
    name: "Chicken Parmesan Meatballs",
    url: "/recipes/chicken-parmesan-meatballs.html",
    texture: "Soft",
    flavor: "Mild",
    continent: "Dinner Dell",
    ingredients: ["ground chicken", "breadcrumbs", "cheese"]
  },
  {
    name: "Ground Beef Noodle Casserole",
    url: "/recipes/ground-beef-noodle-casserole.html",
    texture: "Soft",
    flavor: "Mild",
    continent: "Dinner Dell",
    ingredients: ["pasta", "ground beef", "cheese"]
  },
  {
    name: "Chicken Alfredo",
    url: "/recipes/chicken-alfredo.html",
    texture: "Smooth",
    flavor: "Mild",
    continent: "Dinner Dell",
    ingredients: ["chicken", "pasta", "alfredo sauce"]
  },
  {
    name: "French Bread Pizza",
    url: "/recipes/french-bread-pizza.html",
    texture: "Crisp",
    flavor: "Mild",
    continent: "Dinner Dell",
    ingredients: ["bread", "pizza sauce", "cheese"]
  },
  {
    name: "Sesame Chicken Meatballs",
    url: "/recipes/sesame-chicken-meatballs.html",
    texture: "Soft",
    flavor: "Sweet",
    continent: "Dinner Dell",
    ingredients: ["ground chicken", "honey", "ginger"]
  },
  {
    name: "Chili Dog Casserole",
    url: "/recipes/chili-dog-casserole.html",
    texture: "Crisp",
    flavor: "Mild",
    continent: "Dinner Dell",
    ingredients: ["hot dogs", "cornbread mix", "cheese"]
  },
  {
    name: "Strawberry Cream Pops",
    url: "/recipes/strawberry-cream-pops.html",
    texture: "Smooth",
    flavor: "Sweet",
    continent: "Dessert Dunes",
    ingredients: ["strawberries", "yogurt", "honey"]
  },
  {
    name: "Homemade Dunkaroos",
    url: "/recipes/homemade-dunkaroos.html",
    texture: "Crisp",
    flavor: "Sweet",
    continent: "Dessert Dunes",
    ingredients: ["shortbread cookies", "frosting", "sprinkles"]
  },
  {
    name: "Rainbow Fruit Skewers",
    url: "/recipes/rainbow-fruit-skewers.html",
    texture: "Crisp",
    flavor: "Sweet",
    continent: "Dessert Dunes",
    ingredients: ["strawberries", "pineapple", "grapes"]
  },
  {
    name: "Chocolate Banana Bites",
    url: "/recipes/chocolate-banana-bites.html",
    texture: "Smooth",
    flavor: "Sweet",
    continent: "Dessert Dunes",
    ingredients: ["banana", "chocolate", "peanuts"]
  },
  {
    name: "Peanut Butter Cookies",
    url: "/recipes/peanut-butter-cookies.html",
    texture: "Crisp",
    flavor: "Sweet",
    continent: "Dessert Dunes",
    ingredients: ["peanut butter", "sugar", "flour"]
  },
  {
    name: "Apple Pie Bites",
    url: "/recipes/apple-pie-bites.html",
    texture: "Crisp",
    flavor: "Sweet",
    continent: "Dessert Dunes",
    ingredients: ["apple", "cinnamon", "pastry"]
  },
  {
    name: "Yogurt Fruit Pops",
    url: "/recipes/yogurt-fruit-pops.html",
    texture: "Smooth",
    flavor: "Sweet",
    continent: "Dessert Dunes",
    ingredients: ["yogurt", "berries", "honey"]
  },
  {
    name: "Oatmeal Raisin Bars",
    url: "/recipes/oatmeal-raisin-bars.html",
    texture: "Soft",
    flavor: "Sweet",
    continent: "Dessert Dunes",
    ingredients: ["oats", "raisins", "brown sugar"]
  }
];

// Recipe Finder logic (assumed, update as needed)
function findRecipes() {
  // Example: Filter recipes based on texture, flavor, and dislikes
  // Outputs links like <a href="/recipes/mini-pancake-bites.html">Mini Pancake Bites</a>
}
{
  name: "Yogurt Parfait",
  url: "/recipes/yogurt-parfait.html",
  texture: "Smooth",
  flavor: "Sweet",
  continent: "Breakfast Bays",
  ingredients: ["yogurt", "granola", "fruit"]
}
{
  name: "Pumpkin Protein Muffins",
  url: "/recipes/pumpkin-protein-muffins.html",
  texture: "Soft",
  flavor: "Sweet",
  continent: "Breakfast Bays",
  ingredients: ["pumpkin puree", "flour", "protein powder"]
}
