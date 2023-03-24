import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'food_for_thought.settings')

import django, datetime

django.setup()
from recipes.models import Category, Recipe, UserProfile, Review, User
from django.core.files.images import ImageFile


def get_user(username):
    return User.objects.get(username=username)


def get_userprofile(username):
    user = get_user(username)
    return UserProfile.objects.get(user=user)


def get_category(name):
    return Category.objects.get(name=name)


def get_recipe(title):
    return Recipe.objects.get(title=title)


def populate():
    categories = [{
        "name": "Baked",
        "image": "static/category_images/baked_category.jpg",
        "description": "Here find some amazing baked goods for all occasions that will have you and your guests "
                       "wanting seconds!"
    }, {
        "name": "Fried",
        "image": "static/category_images/fried_category.jpg",
        "description": "Sometimes all you want is a traditional fry up. Find all your fried desires here!"
    }, {
        "name": "Breakfast",
        "image": "static/category_images/breakfast_category.jpg",
        "description": "From Croissants to Overnight oats, you'll find your morning craving in this category!"
    }, {
        "name": "Lunch",
        "image": "static/category_images/lunch_category.jpg",
        "description": "How about some pasta? Oh or a salad! Or maybe even a toastie! Or maybe you're just looking "
                       "for ways to spice up your packed lunch box. You can find all that and more here."
    }, {
        "name": "Dinner",
        "image": "static/category_images/dinner_category.jpg",
        "description": "Simple bolognese to steak or maybe even a Sunday roast. Find the tastiest meals for even the fusiest eaters below."
    }, {
        "name": "Dessert",
        "image": "static/category_images/dessert_category.jpg",
        "description": "Cake? Muffins? Pie? Fruit salad? Something delicious but healthy? Yes to all of it, please!"
    }, {
        "name": "Vegetarian",
        "image": "static/category_images/vegetarian_category.jpg",
        "description": "Find below protein full, delicious and completely vegetarian recipes for the enjoyment of all!"
    }, {
        "name": "Pasta",
        "image": "static/category_images/pasta_category.jpg",
        "description": "Truly a favourite for all. Find your next tasty pasta dish from simple recipes to recipes that "
                       "will make you think you're sitting in a restaurant in the middle of Rome."
    },
    ]

    for category in categories:
        c = Category.objects.get_or_create(name=category["name"])[0]
        with open(category["image"], "rb") as i:
            c.image = ImageFile(i)
            c.description = category["description"]
            c.save()

    users = [{
        "auth": {"username": "paul", "password": "1234", "firstname": "Paul", "lastname": "Davids",
                 "email": "pauldavids@gmail.com"},
        "profile": {
            "bio": "I like to cook!",
            "picture": "static/profile_images/paul.jpg",
        },
        "recipes": [{
            "title": "Bread",
            "category": {"Baked"},
            "ingredients": "500g strong white flour, plus extra for dusting, "
                           "2 tsp salt, "
                           "7g sachet fast-action yeast, "
                           "3 tbsp olive oil, "
                           "300ml water.",
            "content": "STEP 1: "
                       "Mix 500g strong white flour, 2 tsp salt and a 7g sachet of fast-action yeast in a large bowl. "
                       "STEP 2: "
                       "Make a well in the centre, then add 3 tbsp olive oil and 300ml water, and mix well. If the "
                       "dough seems a little stiff, add another 1-2 tbsp water and mix well. "
                       "STEP 3: "
                       "Tip onto a lightly floured work surface and knead for around 10 mins. "
                       "STEP 4: "
                       "Once the dough is satin-smooth, place it in a lightly oiled bowl and cover with cling film. "
                       "Leave to rise for 1 hour until doubled in size or place in the fridge overnight. "
                       "STEP 5: "
                       "Line a baking tray with baking parchment. Knock back the dough (punch the air out and pull "
                       "the dough in on itself) then gently mould the dough into a ball. "
                       "STEP 6: "
                       "Place it on the baking parchment to prove for a further hour until doubled in size. "
                       "STEP 7: "
                       "Heat oven to 220C/fan 200C/gas 7. "
                       "STEP 8: "
                       "Dust the loaf with some extra flour and cut a cross about 6cm long into the top of the loaf "
                       "with a sharp knife. "
                       "STEP 9: "
                       "Bake for 25-30 mins until golden brown and the loaf sounds hollow when tapped underneath. "
                       "Cool on a wire rack.",
            "cooking_time": datetime.timedelta(minutes=50),
            "image": "static/recipe_images/bread.jpg",
            "servings": "1",
            "tags": "#quick #yum #homemade #fresh"
        },
            {"title": "Croissants",
             "category": {"Breakfast", "Dessert"},
             "ingredients": "500g strong white flour, plus extra for dusting, "
                            "1 ½ tsp salt, "
                            "50g sugar, "
                            "2 x 7g sachets fast-action dried yeast, "
                            "oil, for greasing, "
                            "300g butter, at room temperature, "
                            "1 egg, beaten.",
             "content": "STEP 1: "
                        "Put the flour, salt and sugar in a mixing bowl. Measure 300ml cold water into a jug, "
                        "add the yeast and stir. Make a well in the flour and pour in the liquid. Mix, then knead on "
                        "your work surface for 10 mins. Shape into a ball, put in a lightly oiled bowl, "
                        "cover and chill for at least 2 hrs. "
                        "STEP 2: "
                        "Put the butter between 2 sheets of baking parchment. Using a rolling pin, bash and roll it "
                        "into a rectangle about 20 x 15cm. Leave wrapped in the baking parchment and chill. "
                        "STEP 3: "
                        "Transfer the chilled dough to a floured surface and roll into a 40 x 20cm rectangle. Place "
                        "the unwrapped slab of butter in the centre of the dough, so that it covers the middle third. "
                        "STEP 4: "
                        "Fold one side of the dough up and halfway over the butter. "
                        "STEP 5: "
                        "Fold the other side of the dough up and over the butter in the same way, so that the two "
                        "edges of the dough meet in the centre of the butter. "
                        "STEP 6: "
                        "Fold the dough in half so that the point where the ends of the dough meet becomes the seam. "
                        "Wrap in cling film and chill for 30 mins. "
                        "STEP 7: "
                        "Repeat the rolling, folding and chilling process (steps 3-6) twice more in exactly the same "
                        "way – rolling the pastry while it’s still folded – without adding more butter. Wrap and "
                        "chill overnight. "
                        "STEP 8: "
                        "The next day, roll the dough out on a floured surface into a large rectangle, measuring "
                        "about 60 x 30cm. Using a sharp knife or pizza cutter, trim the edges to neaten. "
                        "STEP 9: "
                        "Cut the dough in half lengthways so that you have 2 long strips, then cut each strip into 6 "
                        "or 7 triangles with 2 equal sides. "
                        "STEP 10: "
                        "Take each triangle in turn and pull the two corners at the base to stretch and widen it. "
                        "STEP 11: "
                        "Starting at the base of each triangle, begin to gently roll into a croissant, being careful "
                        "not to crush the dough. "
                        "STEP 12: "
                        "Continue rolling, making sure the tip of each triangle ends up tucked under the croissant to "
                        "hold in place. If adding any fillings (see tips, below), place across the widest part of the "
                        "triangle before rolling up. "
                        "STEP 13: "
                        "Bend the ends of the croissants inwards, then transfer to baking trays lined with baking "
                        "parchment, spaced well apart. Cover with lightly oiled cling film and leave to rise for 2 "
                        "hrs, or until doubled in size. "
                        "STEP 14: "
                        "Heat oven to 200C/180C fan/gas 6. Mix the beaten egg with a pinch of salt and use to "
                        "generously glaze the croissants. Bake for 15-18 mins until risen and golden brown, "
                        "then cool on wire racks.",
             "cooking_time": datetime.timedelta(hours=1, minutes=30),
             "image": "static/recipe_images/croissants.jpg",
             "servings": "12",
             "tags": "#Tricky #Yum #Pastry #French",
             },
            {"title": "Chicken Satay Salad",
             "category": {"Lunch"},
             "ingredients": "1 tbsp tamari, "
                            "1 tsp medium curry powder, "
                            "¼ tsp ground cumin, "
                            "1 garlic clove, finely grated, "
                            "1 tsp clear honey, "
                            "2 skinless chicken breast fillets (or use turkey breast), "
                            "1 tbsp crunchy peanut butter (choose a sugar-free version with no palm oil, if possible), "
                            "1 tbsp sweet chilli sauce, "
                            "1 tbsp lime juice, "
                            "sunflower oil, for wiping the pan, "
                            "2 Little Gem lettuce hearts, cut into wedges, "
                            "¼ cucumber, halved and sliced, "
                            "1 banana shallot, halved and thinly sliced, "
                            "coriander, chopped, "
                            "seeds from ½ pomegranate.",
             "content": "STEP 1: "
                        "Pour the tamari into a large dish and stir in the curry powder, cumin, garlic and honey. Mix "
                        "well. Slice the chicken breasts in half horizontally to make 4 fillets in total, then add to "
                        "the marinade and mix well to coat. Set aside in the fridge for at least 1 hr, or overnight, "
                        "to allow the flavours to penetrate the chicken. "
                        "STEP 2: "
                        "Meanwhile, mix the peanut butter with the chilli sauce, lime juice, and 1 tbsp water to make "
                        "a spoonable sauce. When ready to cook the chicken, wipe a large non-stick frying pan with a "
                        "little oil. Add the chicken and cook, covered with a lid, for 5-6 mins on a medium heat, "
                        "turning the fillets over for the last min, until cooked but still moist. Set aside, covered, "
                        "to rest for a few mins. "
                        "STEP 3: "
                        "While the chicken rests, toss the lettuce wedges with the cucumber, shallot, coriander and "
                        "pomegranate, and pile onto plates. Spoon over a little sauce. Slice the chicken, pile on top "
                        "of the salad and spoon over the remaining sauce. Eat while the chicken is still warm.",
             "cooking_time": datetime.timedelta(minutes=30),
             "image": "static/recipe_images/chicken_satay_salad.jpg",
             "servings": "2",
             "tags": "#healthy #chicken #salad",
             },
        ]
    }, {
        "auth": {"username": "mrbean62", "password": "1234", "firstname": "Ben", "lastname": "Oak",
                 "email": "benoak@gmail.com"},
        "profile": {
            "bio": "havin fun",
            "picture": "static/profile_images/mrbean62.jpg",
        },
        "recipes": [{"title": "Chocolate Fudge Cake",
                     "category": {"Dessert", "Baked"},
                     "ingredients": "150ml sunflower oil, plus extra for the tin, "
                                    "175g self-raising flour, "
                                    "2 tbsp cocoa powder, "
                                    "1 tsp bicarbonate of soda, "
                                    "150g caster sugar, "
                                    "2 tbsp golden syrup, "
                                    "2 large eggs, lightly beaten, "
                                    "150ml semi-skimmed milk. "
                                    "For the icing: "
                                    "100g unsalted butter, "
                                    "225g icing sugar, "
                                    "40g cocoa powder, "
                                    "2½ tbsp milk (a little more if needed).",
                     "content": "STEP 1: "
                                "Heat the oven to 180C/160C fan/gas 4. Oil and line the base of two 18cm sandwich "
                                "tins. Sieve the flour, cocoa powder and bicarbonate of soda into a bowl. Add the "
                                "caster sugar and mix well. "
                                "STEP 2: "
                                "Make a well in the centre and add the golden syrup, eggs, sunflower oil and milk. "
                                "Beat well with an electric whisk until smooth. "
                                "STEP 3: "
                                "Pour the mixture into the two tins and bake for 25-30 mins until risen and firm to "
                                "the touch. Remove from oven, leave to cool for 10 mins before turning out onto a "
                                "cooling rack. "
                                "STEP 4: "
                                "To make the icing, beat the unsalted butter in a bowl until soft. Gradually sieve "
                                "and beat in the icing sugar and cocoa powder, then add enough of the milk to make "
                                "the icing fluffy and spreadable. "
                                "STEP 5: "
                                "Sandwich the two cakes together with the butter icing and cover the sides and the "
                                "top of the cake with more icing.",
                     "cooking_time": datetime.timedelta(hours=1),
                     "image": "static/recipe_images/chocolate_fudge_cake.jpg",
                     "servings": "8",
                     "tags": "#easy #chocolate #cake",
                     },
                    {"title": "Spinach, Sweet Potato & Lentil Dhal",
                     "category": {"Vegetarian", "Lunch"},
                     "ingredients": "1 tbsp sesame oil, "
                                    "1 red onion, finely chopped, "
                                    "1 garlic clove, crushed, "
                                    "thumb-sized piece ginger, peeled and finely chopped, "
                                    "1 red chilli, finely chopped, "
                                    "1½ tsp ground turmeric, "
                                    "1½ tsp ground cumin, "
                                    "2 sweet potatoes (about 400g/14oz), cut into even chunks, "
                                    "250g red split lentils, "
                                    "600ml vegetable stock, "
                                    "80g bag of spinach, "
                                    "4 spring onions, sliced on the diagonal, to serve, "
                                    "½ small pack of Thai basil, leaves torn, to serve.",
                     "content": "STEP 1: "
                                "Heat 1 tbsp sesame oil in a wide-based pan with a tight-fitting lid. "
                                "STEP 2: "
                                "Add 1 finely chopped red onion and cook over a low heat for 10 mins, stirring "
                                "occasionally, until softened. "
                                "STEP 3: "
                                "Add 1 crushed garlic clove, a finely chopped thumb-sized piece of ginger and 1 "
                                "finely chopped red chilli, cook for 1 min, then add 1½ tsp ground turmeric and 1½ "
                                "tsp ground cumin and cook for 1 min more. "
                                "STEP 4: "
                                "Turn up the heat to medium, add 2 sweet potatoes, cut into even chunks, and stir "
                                "everything together so the potato is coated in the spice mixture. "
                                "STEP 5: "
                                "Tip in 250g red split lentils, 600ml vegetable stock and some seasoning. "
                                "STEP 6: "
                                "Bring the liquid to the boil, then reduce the heat, cover and cook for 20 mins until "
                                "the lentils are tender and the potato is just holding its shape. "
                                "STEP 7: "
                                "Taste and adjust the seasoning, then gently stir in the 80g spinach. Once wilted, "
                                "top with the 4 diagonally sliced spring onions and ½ small pack torn basil leaves to "
                                "serve. "
                                "STEP 8: "
                                "Alternatively, allow to cool completely, then divide between airtight containers and "
                                "store in the fridge for a healthy lunchbox.",
                     "cooking_time": datetime.timedelta(minutes=45),
                     "image": "static/recipe_images/spinach_sweet_potato_lentil_dhal.jpg",
                     "servings": "4",
                     "tags": "#vegetarian #healthy #easy #Indian",
                     },
                    {"title": "Creamy Mushroom Pasta",
                     "category": {"Dinner", "Pasta", "Vegetarian"},
                     "ingredients": "2 tbsp olive oil, "
                                    "1 tbsp butter, "
                                    "1 onion, finely chopped, "
                                    "250g button chestnut mushroom, sliced, "
                                    "1 garlic clove, finely grated, "
                                    "100ml dry white wine, "
                                    "200ml double cream, "
                                    "1 lemon, zest only, "
                                    "200g parmesan (or vegetarian alternative), grated, plus extra to serve, "
                                    "300g tagliatelle or linguini, "
                                    "½ small bunch parsley, finely chopped.",
                     "content": "STEP 1: "
                                "Heat the oil and butter in a medium saucepan. Fry the onion over a low heat for 10 "
                                "mins or until softened and translucent. "
                                "STEP 2: "
                                "Add the mushrooms and cook for 10 mins over a medium heat. Add the garlic and cook "
                                "for 2 mins. Add the wine and bring to a simmer, reduce the liquid by half. "
                                "STEP 3: "
                                "Add the double cream and bring to a simmer, then add the lemon zest and parmesan. "
                                "Season with salt and plenty of black pepper. "
                                "STEP 4: "
                                "Meanwhile, cook the pasta following pack instructions. Reserve 100ml of the pasta "
                                "water. Toss the pasta in the pan with the creamy sauce and enough of the reserved "
                                "water to loosen. Stir through the parsley, divide into bowls and top with extra "
                                "cheese, if you like.",
                     "cooking_time": datetime.timedelta(minutes=40),
                     "image": "static/recipe_images/creamy_mushroom_pasta.jpg",
                     "servings": "4",
                     "tags": "#mushrooms #parmesan #easy",
                     },
                    ]
    }, {
        "auth": {"username": "coolboy4572", "password": "1234", "firstname": "Thomas", "lastname": "Board",
                 "email": "thomasboard@gmail.com"},
        "profile": {
            "bio": "havin more fun",
            "picture": "static/profile_images/coolboy4572.jpg",
        },
        "recipes": [{
            "title": "Seafood Rice",
            "category": {"Fried", "Dinner"},
            "ingredients": "1 tbsp olive oil, "
                           "1 leek or onion, sliced, "
                           "110g pack chorizo sausage, chopped, "
                           "1 tsp turmeric, "
                           "300g long grain rice, "
                           "1l hot fish or chicken stock, "
                           "200g frozen peas, "
                           "400g frozen seafood mix, defrosted.",
            "content": "STEP 1: "
                       "Heat the oil in a deep frying pan, then soften the leek for 5 mins without browning. Add the "
                       "chorizo and fry until it releases its oils. Stir in the turmeric and rice until coated by the "
                       "oils, then pour in the stock. Bring to the boil, then simmer for 15 mins, "
                       "stirring occasionally. "
                       "STEP 2: "
                       "Tip in the peas and cook for 5 mins, then stir in the seafood to heat through for a final 1-2 "
                       "mins cooking or until rice is cooked. Check for seasoning and serve immediately with lemon "
                       "wedges.",
            "cooking_time": datetime.timedelta(minutes=30),
            "image": "static/recipe_images/seafood_rice.jpg",
            "servings": "4",
            "tags": "#easy #healthy",
        },
            {"title": "Pepper, Tomato & Ham Omelette",
             "category": {"Fried", "Breakfast"},
             "ingredients": "2 whole eggs and 3 egg whites, "
                            "1 tsp olive oil, "
                            "1 red pepper, deseeded and finely chopped, "
                            "2 spring onions, white and green parts kept separate, and finely chopped, "
                            "few slices wafer-thin extra-lean ham, shredded, "
                            "25g reduced-fat mature cheddar, "
                            "wholemeal toast, to serve (optional), "
                            "1-2 chopped fresh tomatoes, to serve (optional).",
             "content": "STEP 1: "
                        "Mix the eggs and egg whites with some seasoning and set aside. Heat the oil in a medium "
                        "non-stick frying pan and cook the pepper for 3-4 mins. Throw in the white parts of the "
                        "spring onions and cook for 1 min more. Pour in the eggs and cook over a medium heat until "
                        "almost completely set. "
                        "STEP 2: "
                        "Sprinkle on the ham and cheese, and continue cooking until just set in the centre, or flash "
                        "it under a hot grill if you like it more well done. Serve straight from the pan with the "
                        "green part of the spring onions sprinkled on top, the chopped tomato and some wholemeal "
                        "toast, if you like.",
             "cooking_time": datetime.timedelta(minutes=25),
             "image": "static/recipe_images/pepper_tomato_ham_omelette.jpg",
             "servings": "2",
             "tags": "#eggs #healthy #easy",
             },
            {"title": "Fajita-Style Pasta",
             "category": {"Pasta", "Dinner"},
             "ingredients": "2 tbsp olive oil, "
                            "2 large skinless chicken breasts, cut into strips, "
                            "1 onion, thinly sliced, "
                            "1 red pepper, deseeded and sliced, "
                            "1 yellow pepper, deseeded and sliced, "
                            "1 garlic clove, crushed, "
                            "1⁄4 tsp chilli powder, "
                            "1 heaped tsp sweet smoked paprika, "
                            "1⁄2 tsp dried oregano, "
                            "1 tsp ground coriander, "
                            "1⁄2 tsp ground cumin, "
                            "3 tbsp tomato purée, "
                            "80ml double cream, "
                            "350g penne or rigatoni pasta, "
                            "1⁄2 small bunch of flat-leaf parsley, finely chopped, "
                            "grated parmesan or cheddar, to serve.",
             "content": "STEP 1: "
                        "Heat the oil in a large shallow casserole or frying pan. Add the chicken and fry for 5 mins "
                        "over a medium heat until golden all over. Remove and set aside on a plate. "
                        "STEP 2: "
                        "Put the onion and peppers in the same pan and fry over a medium heat for 8-10 mins. Add the "
                        "garlic, dried herbs and spices and cook for 1 min. Add the tomato purée and cook for 2 mins. "
                        "Return the chicken to the pan and pour in the cream, stirring to combine. Season to taste. "
                        "STEP 3: "
                        "Cook the pasta following pack instructions, then drain and reserve 150ml of the cooking "
                        "water. Add the pasta to the pan with 50ml of the water and stir everything together over the "
                        "heat. Add a little more water to loosen if needed. Season to taste and stir through the "
                        "parsley. Divide between six bowls and top with a little cheese and extra chopped parsley, "
                        "if you like. This can be packed into a lunchbox and eaten cold, too.",
             "cooking_time": datetime.timedelta(minutes=35),
             "image": "static/recipe_images/fajita_style_pasta.jpg",
             "servings": "6",
             "tags": "#fajita #spice #easy",
             },
        ]
    }, {
        "auth": {"username": "chefSteph", "password": "1234", "firstname": "Stephanie", "lastname": "Rule",
                 "email": "stephanierule@gmail.com"},
        "profile": {
            "bio": "Professional Chef with 10 years experience working in competitive restaurants. My greatest joy is "
                   "creating and sharing good food and continually learning new skills i the kitchen!",
            "picture": "static/profile_images/chefSteph.jpg",
        },
        "recipes": [{"title": "Pea, Feta & Quinoa Spring Rolls",
                     "category": {"Vegetarian"},
                     "ingredients": "50g quinoa, "
                                    "200g frozen petits pois, "
                                    "85g feta cheese, crumbled, "
                                    "small bunch mint leaves, chopped, "
                                    "3 spring onions, finely chopped, "
                                    "zest and juice 1 lemon, "
                                    "6 sheets filo pastry (270g pack), "
                                    "1 egg, beaten, "
                                    "sunflower oil, for frying. "
                                    "For the nam prik: "
                                    "6 large tomatoes, halved, "
                                    "4 tbsp extra-virgin olive oil, "
                                    "1 garlic clove, chopped, "
                                    "½ red chilli, chopped, "
                                    "2 tsp grated ginger, "
                                    "½ bunch coriander including stalks, roughly chopped, "
                                    "¼ bunch mint leaves, roughly chopped, "
                                    "1 tbsp lime juice, "
                                    "1 tbsp tamarind paste, "
                                    "1 tsp palm sugar.",
                     "content": "STEP 1: "
                                "Heat oven to 160C/140C fan/gas 3. To make the nam prik, place the tomatoes, cut-side "
                                "up, on a baking sheet. Drizzle with 1 tbsp of the olive oil, season, then roast for "
                                "1½-2 hrs until semi-dried. Remove from the oven, let cool, then tip into a food "
                                "processor with the remaining ingredients and blitz to a medium purée. "
                                "STEP 2: "
                                "Cook the quinoa in a pan of boiling salted water following pack instructions. Tip "
                                "into a bowl and set aside to cool. Cook the peas for 1 min in boiling water, "
                                "then drain and run under cold water for a few mins. Drain thoroughly, tip into a "
                                "food processor and pulse to a chunky purée. Add this to the cooled quinoa along with "
                                "the feta, mint, spring onions and lemon zest and juice. Mix well to combine and "
                                "season to taste, adding more lemon juice if required. "
                                "STEP 3: "
                                "Lay a sheet of filo in front of you, keeping the remainder covered under a damp tea "
                                "towel. Cut the filo in half across the width to make 2 squares. With one corner "
                                "pointing towards you (so you are looking at a diamond shape rather than a square), "
                                "spoon 2 tbsp of the filling just below the centre line and shape into a log. Brush "
                                "the pastry edges with egg, then fold in the 2 side corners. Keeping your fingers on "
                                "the corners, bring the bottom corner up over the filling towards the centre, "
                                "then roll up tightly towards the top corner. It’s important to roll as tightly as "
                                "possible, so the spring rolls cook evenly. Repeat with the remaining filo sheets and "
                                "filling. "
                                "STEP 4: "
                                "Heat about 3cm sunflower oil in a large pan or wok and fry the spring rolls, "
                                "in batches, for 2-3 mins or until golden brown. Remove with a slotted spoon and "
                                "drain on kitchen paper. Transfer the spring rolls to a plate and serve with the nam "
                                "prik.",
                     "cooking_time": datetime.timedelta(hours=2, minutes=40),
                     "image": "static/recipe_images/pea_feta_spring_rolls.jpg",
                     "servings": "12",
                     "tags": "#difficult #springrolls #Chinese #snack",
                     },
                    {"title": "Toffee Apple Cake",
                     "category": {"Dessert", "Baked"},
                     "ingredients": "150ml vegetable oil, plus extra for greasing, "
                                    "175g dark brown soft sugar, "
                                    "2 large eggs, "
                                    "250g eating apples (prepared weight – about 3 apples), peeled, cored and coarsely grated, "
                                    "200g self-raising flour, "
                                    "2 tsp ground cinnamon, "
                                    "1 tsp ground ginger, "
                                    "1 tsp bicarbonate of soda, "
                                    "25g rolled oats, "
                                    "50g ground almonds, "
                                    "100g sultanas, "
                                    "zest 1 lemon. "
                                    "For the filling and decoration: "
                                    "juice 1 lemon, "
                                    "4 eating apples (I used Pink Lady), "
                                    "25g butter, "
                                    "50g dark brown soft sugar, "
                                    "1 tbsp golden syrup, "
                                    "¼ tsp cinnamon, "
                                    "100g white caster sugar (optional, for the tiny toffee apples). "
                                    "For the syrup: "
                                    "75g dark brown soft sugar, "
                                    "juice 1 lemon, "
                                    "1 tbsp brandy, or water. "
                                    "For the icing: "
                                    "50g butter, "
                                    "100g white chocolate, "
                                    "280g tub cream cheese, "
                                    "1 vanilla pod, seeds only, "
                                    "170g pot Greek yogurt. "
                                    "You will need: "
                                    "8 long wooden skewers (optional, for the tiny toffee apples).",
                     "content": "STEP 1: "
                                "Start by making the cakes. Heat oven to 180C/160C fan/gas 4. Line 2 x 18cm "
                                "springform cake tins with baking parchment and brush with a little oil. Put the "
                                "sugar and eggs in a large mixing bowl and whisk with electric beaters until glossy "
                                "and pale. Keep the beaters running as you pour in the oil. "
                                "STEP 2: "
                                "Stir in the grated apple, then fold in all the other cake ingredients. Divide the "
                                "mixture between the tins and bake for 30 mins or until a skewer inserted into the "
                                "middle comes out clean. "
                                "STEP 3: "
                                "While the cakes cook, prepare the apple filling. Tip the lemon juice into a large "
                                "bowl and fill halfway with cold water. Peel the apples, then cut into spheres using "
                                "a melon baller – pop them in the bowl of lemon water as you go to stop them "
                                "discolouring. In a medium saucepan, combine the butter, dark brown sugar, "
                                "golden syrup, cinnamon and 200ml water, and heat until boiling. Take the apple balls "
                                "out of the water and put them in the pan –if you want to make the tiny toffee apples "
                                "for the top, keep 8 apple balls in the water until needed. Bring the mixture in the "
                                "pan back to the boil for 8 - 10 mins or until the apples are soft but not losing "
                                "their shape, and a thick syrup starts to form. Remove from the heat and allow to "
                                "cool completely, then chill until needed. "
                                "STEP 4: "
                                "Stir all the syrup ingredients together in a bowl. When the cakes are cooked, "
                                "keep them in the tin but prick holes all over the surface with a skewer and drizzle "
                                "the syrup over. Leave the cakes to cool completely in the tin. "
                                "STEP 5: "
                                "While the cakes cool, make the icing. In a small heatproof bowl set over a pan of "
                                "simmering water, melt the butter and white chocolate together. Once melted and "
                                "glossy, pour into a large bowl. Add the cream cheese, whisk until smooth, "
                                "then add the vanilla. Finally, fold in the yogurt. When the mixture is cool, "
                                "chill until needed. "
                                "STEP 6: "
                                "To assemble the cake, take the cooled sponges out of their tins and put one of them "
                                "on a cake stand. Top with half the white chocolate icing – use a spoon or pipe it "
                                "using a very large round nozzle. Scatter the cooked apple pieces, along with a "
                                "drizzle of the syrup, over the icing, then place in the fridge to firm up for 15 "
                                "mins. Add the top layer of the cake, then decorate with the rest of the icing by "
                                "piping it in lots of regular little mounds all over the top using a large round "
                                "nozzle. Put the whole cake in the fridge until ready to serve. Will keep for 2 days "
                                "in the fridge. "
                                "STEP 7: "
                                "For a showstopping, but optional, finish, make some beautiful miniature toffee "
                                "apples. Their effect is stunning but fleeting, so make them just before serving your "
                                "cake, as the caramel will dissolve quickly due to the moisture in the air. Brush a "
                                "baking tray with a little vegetable oil and set aside. Very thoroughly dry the "
                                "reserved apple balls from step 3 of the cake with kitchen paper or a clean tea towel "
                                "and insert a long wooden skewer into each one. "
                                "STEP 8: "
                                "Put the caster sugar in a small saucepan over a medium heat, stirring often, "
                                "until the sugar melts. Keep cooking until the sugar has become a liquid golden "
                                "caramel, then remove from the heat. If it looks like it’s getting too hot, "
                                "sit the base of the pan in a heatproof dish of cold water. "
                                "STEP 9: "
                                "Tilt the pan and, working quickly (as the sugar will continue to cook), hold the "
                                "apple balls by the skewer and dip each one in turn into the caramel and twist it "
                                "around to coat it. It’s really important that the apple balls are well dried and "
                                "that you don’t turn them in the hot caramel more than twice, otherwise the apple "
                                "will cook and release liquid, which will stop the caramel from sticking. As soon as "
                                "they are coated, slowly lift them out vertically. Hold the apple up out of the pan "
                                "and pause before transferring it to the oiled tray on its side. Holding it up like "
                                "this will allow a long drip of caramel to set hard and create a beautiful long "
                                "spike. Repeat the process with the rest of the apples, working quickly so that the "
                                "caramel doesn’t harden completely before all the apples have been coated. However, "
                                "don’t worry too much as you can always gently reheat it over a low heat before "
                                "continuing – just be careful not to burn it, otherwise it will taste bitter. "
                                "STEP 10: "
                                "After a couple of minutes, the apples should have set. When they are cool enough to "
                                "handle, pull out the skewers. Place the apples on top of the cake so that the spike "
                                "is pointing upwards and the base of the apple (where the skewer was) is pressed into "
                                "the icing. Serve immediately.",
                     "cooking_time": datetime.timedelta(hours=1, minutes=35),
                     "image": "static/recipe_images/toffee_apple_cake.jpg",
                     "servings": "16",
                     "tags": "#toffee #apple #sweet #difficult",
                     },
                    {"title": "Chicken Katsue Curry Burger",
                     "category": {"Dinner"},
                     "ingredients": "2 skinless chicken breasts, "
                                    "vegetable oil or sunflower oil, for frying. "
                                    "For the brine: "
                                    "500ml milk, "
                                    "1 garlic clove, crushed, "
                                    "1 tbsp shichimi togarashi (see tip). "
                                    "For the katsu mayo:"
                                    "50ml ketchup, "
                                    "1 tsp toasted sesame oil, "
                                    "1 tsp soy sauce, "
                                    "1 tbsp Worcestershire sauce, "
                                    "½ tbsp runny honey, "
                                    "juice ½ lime, "
                                    "1 tsp hot mustard, "
                                    "2 tsp medium curry powder, "
                                    "3 tbsp mayonnaise. "
                                    "For the chicken katsu: "
                                    "1 egg, "
                                    "100g rice flour, "
                                    "60g panko breadcrumbs, "
                                    "2 burger buns (preferably brioche), "
                                    "handful shredded iceberg lettuce, "
                                    "2 spring onions, finely sliced, "
                                    "2 radishes, finely sliced.",
                     "content": "STEP 1: "
                                "In a bowl, combine the ingredients for the brine with 1 tsp salt. Put the chicken in "
                                "the brine, cover with cling film and marinate in the fridge for at least 3 hrs. "
                                "STEP 2: "
                                "To make the mayo, combine all the ingredients and stir until smooth. "
                                "STEP 3: "
                                "Half an hour before cooking, remove the chicken from the fridge. Crack the egg into "
                                "a bowl and whisk with 2 tbsp of the brine. Mix the rice flour and panko, and spread "
                                "out in a layer on a plate. Remove one chicken breast from the brine, shake off the "
                                "excess, dip into the egg mix, then coat in the panko mix. Transfer to a plate and "
                                "repeat with the other chicken breast. "
                                "STEP 4: "
                                "Heat the oil in a deep-fat fryer or large, heavy-bottomed saucepan until it reaches "
                                "180C, or a piece of bread browns in 30 secs. Fry for 10-12 mins until cooked "
                                "through. Drain on kitchen paper, then slice each breast into 4-5 pieces. "
                                "STEP 5: "
                                "Split and toast the buns, then spread with the mayo. Add a layer of lettuce, "
                                "spring onions and radishes, then top with the chicken and more mayo.",
                     "cooking_time": datetime.timedelta(hours=3, minutes=35),
                     "image": "static/recipe_images/chicken_katsu_burger.jpg",
                     "servings": "2",
                     "tags": "#burgers #Japenese #mediumDifficulty #crispy",
                     },
                    ]
    }, {
        "auth": {"username": "cookByTheBook", "password": "1234", "firstname": "Lizzie", "lastname": "MacIntosh",
                 "email": "lizziemacintosh@gmail.com"},
        "profile": {
            "bio": "Just starting out in the cooking world. Looking for easy recipes and hopefully I'll soon build up "
                   "to difficult recipes! I'm a single mum of 3 so am constantly looking for healthy but delicious "
                   "food that even my fussy eaters will devour.",
            "picture": "static/profile_images/cookByTheBook.jpg",
        },
        "recipes": [{"title": "Roasted Sweet Potato & Carrot Soup",
                     "category": {"Lunch", "Vegetarian"},
                     "ingredients": "500g sweet potatoes, peeled and cut into chunks, "
                                    "300g carrots, peeled and cut into chunks, "
                                    "3 tbsp olive oil, "
                                    "2 onions, finely chopped, "
                                    "2 garlic cloves, crushed, "
                                    "1l vegetable stock, "
                                    "100ml crème fraîche, plus extra to serve.",
                     "content": "STEP 1: "
                                "Heat oven to 220C/200C fan/ gas 7 and put 500g chunked sweet potatoes and 300g "
                                "chunked carrots into a large roasting tin, drizzled with 2 tbsp olive oil and plenty "
                                "of seasoning. "
                                "STEP 2: "
                                "Roast the vegetables in the oven for 25-30 mins or until caramelised and tender. "
                                "STEP 3: "
                                "Meanwhile, put the remaining 1 tbsp olive oil in a large deep saucepan and fry 2 "
                                "finely chopped onions over a medium-low heat for about 10 mins until softened. "
                                "STEP 4: "
                                "Add 2 crushed garlic cloves and stir for 1 min before adding 1l vegetable stock. "
                                "Simmer for 5-10 mins until the onions are very soft, then set aside. "
                                "STEP 5: "
                                "Once the roasted vegetables are done, leave to cool a little, then transfer to the "
                                "saucepan and use a hand blender to process until smooth. Stir in 100ml crème "
                                "fraîche, a little more seasoning and reheat until hot. "
                                "STEP 6: "
                                "Serve in bowls topped with a swirl of crème fraîche and a good grinding of black "
                                "pepper.",
                     "cooking_time": datetime.timedelta(minutes=50),
                     "image": "static/recipe_images/sweet_potato_carrot_soup.jpg",
                     "servings": "4",
                     "tags": "#easy #warm #soup #comforting",
                     },
                    {"title": "Brioche Breakfast Bake with Crispy Bacon",
                     "category": {"Breakfast", "Baked"},
                     "ingredients": "3 large eggs, "
                                    "150ml double cream, "
                                    "200ml milk, "
                                    "2 tbsp maple syrup, plus extra to serve, "
                                    "2 tsp vanilla extract, "
                                    "200g punnet blueberries, "
                                    "8 brioche rolls, each one split in half (if your dish is shallow, cut in half "
                                    "again the other way to make shorter pieces),"
                                    "50g pecan halves, "
                                    "6-8 rashers of your favourite bacon, "
                                    "icing sugar, for dusting.",
                     "content": "STEP 1: "
                                "In a large bowl, whisk together the eggs, cream, milk, maple syrup, vanilla and a "
                                "pinch of salt. Tip about two-thirds of the blueberries into a baking dish (about "
                                "20cm x 30cm) that is quite deep. Dip each brioche piece into the egg mixture until "
                                "well soaked, then arrange on top on the blueberries and pour any remaining egg "
                                "mixture over the top. Scatter over the remaining blueberries. Cover with cling film "
                                "and chill for 1 hr, or overnight if serving it for breakfast. "
                                "STEP 2: "
                                "Heat oven to 180C/160C fan/gas 4. Uncover the dish and scatter over the pecans. Bake "
                                "for 25 mins until the egg mixture is set and the blueberries are starting to burst. "
                                "Meanwhile, line a baking tray with foil and arrange the bacon on top. When the "
                                "brioche bake is ready, remove from the oven and cover loosely with foil to keep "
                                "warm. Heat the grill to high and cook the bacon for about 5 mins each side until "
                                "crispy. "
                                "STEP 3: "
                                "Dust the brioche bake with icing sugar and top with the crispy bacon. Serve with "
                                "extra maple syrup for drizzling. ",
                     "cooking_time": datetime.timedelta(hours=2),
                     "image": "static/recipe_images/brioche_bake_bacon.jpg",
                     "servings": "6",
                     "tags": "#crispy #delicious #sweet #easy",
                     },
                    {"title": "Pasta with Salmon & Peas",
                     "category": {"Pasta", "Dinner"},
                     "ingredients": "240g wholewheat fusilli, "
                                    "knob of butter, "
                                    "1 large shallot, finely chopped, "
                                    "140g frozen peas, "
                                    "2 skinless salmon fillets, cut into chunks, "
                                    "140g low-fat crème fraîche, "
                                    "½ low-salt vegetable stock cube, "
                                    "small bunch of chives, snipped.",
                     "content": "STEP 1: "
                                "Bring a pan of water to the boil and cook the fusilli according to the pack "
                                "instructions. "
                                "STEP 2: "
                                "Meanwhile, heat a knob of butter in a saucepan, then add the shallot and cook for 5 "
                                "mins or until softened. "
                                "STEP 3: "
                                "Add the peas, salmon, crème fraîche and 50ml water. Crumble in the stock cube. "
                                "STEP 4: "
                                "Cook for 3-4 mins until cooked through, stir in the chives and some black pepper. "
                                "Then stir through to coat the pasta. Serve in bowls.",
                     "cooking_time": datetime.timedelta(minutes=20),
                     "image": "static/recipe_images/salmon_pasta.jpg",
                     "servings": "4",
                     "tags": "#easy #healthy #quick #lovedByKids",
                     },
                    ]
    }
    ]

    for user in users:
        u = User.objects.create_user(user["auth"]["username"], user["auth"]["email"], user["auth"]["password"])
        u.first_name = user["auth"]["firstname"]
        u.last_name = user["auth"]["lastname"]

        up = UserProfile.objects.get_or_create(**user["profile"], user=u)[0]
        u.save()

        with open(user["profile"]["picture"], "rb") as i:
            up.picture = ImageFile(i)
            up.save()

        for recipe in user["recipes"]:
            r = Recipe.objects.get_or_create(title=recipe["title"], author=u, content=recipe["content"],
                                             ingredients=recipe["ingredients"], cooking_time=recipe["cooking_time"],
                                             servings=recipe["servings"], tags=recipe["tags"])[0]

            for c in recipe["category"]:
                r.category.add(get_category(c))

            with open(recipe["image"], "rb") as i:
                r.image = ImageFile(i)
                r.save()

    get_userprofile("mrbean62").saved.add(get_recipe("Pea, Feta & Quinoa Spring Rolls"))
    get_userprofile("coolboy4572").saved.add(get_recipe("Bread"), get_recipe("Pea, Feta & Quinoa Spring Rolls"),
                                             get_recipe("Croissants"))
    get_userprofile("chefSteph").saved.add(get_recipe("Brioche Breakfast Bake with Crispy Bacon"),
                                           get_recipe("Spinach, Sweet Potato & Lentil Dhal"))
    get_userprofile("cookByTheBook").saved.add(get_recipe("Chocolate Fudge Cake"), get_recipe("Fajita-Style Pasta"))

    reviews = [{
        "author": get_user("coolboy4572"),
        "recipe": get_recipe("Bread"),
        "content": "cool",
        "rating": 5,
    },
        {
            "author": get_user("chefSteph"),
            "recipe": get_recipe("Seafood Rice"),
            "content": "I was surprisingly shocked by how much I loved this simple dish but it truly contains heart "
                       "and is the perfect thing for the end of a long day.",
            "rating": 4,
        },
        {
            "author": get_user("cookByTheBook"),
            "recipe": get_recipe("Chocolate Fudge Cake"),
            "content": "My kids loved this recipe! It's definitely going to be a house favourite. Now if you'll excuse "
                       "me, I need to go restore my kitchen.",
            "rating": 5,
        },
        {
            "author": get_user("paul"),
            "recipe": get_recipe("Creamy Mushroom Pasta"),
            "content": "Wasn't a fan of the mushrooms",
            "rating": 2,
        },
        {
            "author": get_user("mrbean62"),
            "recipe": get_recipe("Toffee Apple Cake"),
            "content": "This was an incredibly difficult recipe but well worth it for the result!",
            "rating": 3,
        },
        {
            "author": get_user("coolboy4572"),
            "recipe": get_recipe("Pea, Feta & Quinoa Spring Rolls"),
            "content": "Was a good snack",
            "rating": 4,
        },
        {
            "author": get_user("chefSteph"),
            "recipe": get_recipe("Fajita-Style Pasta"),
            "content": "Was incredibly bland",
            "rating": 1,
        },
        {
            "author": get_user("cookByTheBook"),
            "recipe": get_recipe("Fajita-Style Pasta"),
            "content": "Love this. Pasta? Fajitas? What's not to love!",
            "rating": 4,
        },
        {
            "author": get_user("paul"),
            "recipe": get_recipe("Chicken Katsue Curry Burger"),
            "content": "Was kind of fiddly but tasted good",
            "rating": 3,
        },
        {
            "author": get_user("mrbean62"),
            "recipe": get_recipe("Chicken Satay Salad"),
            "content": "Nice twist to a usually boring lunch option",
            "rating": 3,
        },
        {
            "author": get_user("coolboy4572"),
            "recipe": get_recipe("Roasted Sweet Potato & Carrot Soup"),
            "content": "Easy and fairly tasty",
            "rating": 3,
        },
        {
            "author": get_user("chefSteph"),
            "recipe": get_recipe("Brioche Breakfast Bake with Crispy Bacon"),
            "content": "Exactly the kind of thing I crave in the mornings, it hit the spot.",
            "rating": 4,
        },
        {
            "author": get_user("cookByTheBook"),
            "recipe": get_recipe("Pepper, Tomato & Ham Omelette"),
            "content": "Was perfect with an added bit of seasoning",
            "rating": 2,
        },
        {
            "author": get_user("paul"),
            "recipe": get_recipe("Spinach, Sweet Potato & Lentil Dhal"),
            "content": "Wayyyy too spicy",
            "rating": 1,
        },
        {
            "author": get_user("mrbean62"),
            "recipe": get_recipe("Pasta with Salmon & Peas"),
            "content": "Not a whole lot of flavour but easy enough",
            "rating": 3,
        },
        {
            "author": get_user("coolboy4572"),
            "recipe": get_recipe("Croissants"),
            "content": "Delicious but a bit tricky",
            "rating": 4,
        },
        {
            "author": get_user("chefSteph"),
            "recipe": get_recipe("Spinach, Sweet Potato & Lentil Dhal"),
            "content": "Perfect flavouring and a real treat to both cook and eat",
            "rating": 5,
        },
        {
            "author": get_user("cookByTheBook"),
            "recipe": get_recipe("Chicken Katsue Curry Burger"),
            "content": "Too tricky for me at the moment it seems, the decostructed mess I did manage to create though "
                       "did taste quite nice.",
            "rating": 3,
        },
        {
            "author": get_user("paul"),
            "recipe": get_recipe("Seafood Rice"),
            "content": "Made me sick",
            "rating": 1,
        },
        {
            "author": get_user("mrbean62"),
            "recipe": get_recipe("Pea, Feta & Quinoa Spring Rolls"),
            "content": "Very nice",
            "rating": 5,
        },
    ]

    for review in reviews:
        r = Review.objects.get_or_create(**review)[0]
        r.save()


if __name__ == "__main__":
    print("Populating database")
    populate()
    print("done")
