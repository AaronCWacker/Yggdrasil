# Version 5


import streamlit as st

# Combined markdown data
WELLNESS_PROGRAM = """
# 🧠 Movement & Wellness Program

## 🎯 Core Training Areas

### 🗡️ Combat Arts
- Stick Fighting Kata
 - Form 1-3: 15 min/daily
 - Shadow patterns: 10 min
 - Partner work: 2x/week
 - GOAL: Flow state in combat movement

### 🩰 Dance & Movement
- Kizomba
 - Base steps: 20 min
 - Partner work: 1hr/week
 - Flow practice: 15 min/daily
 - GOAL: Fluid leading/following

- Body Movement
 - Ground flow: 10 min
 - Animal walks: 15 min
 - Mobility flows: 20 min
 - GOAL: Natural movement mastery

### 🏃 Dynamic Training
- Stair Runs
 - Sprint sets: 10x3
 - Two-step bounds: 8x4
 - Single leg hops: 12 each
 - GOAL: Explosive power

- Agility Drills
 - Ladder work: 5 patterns
 - Cone drills: 3 sets
 - Direction changes: 4x5
 - GOAL: Quick direction change

### 🎯 Precision Work
- Dexterity Training
 - Finger sequences: 5 min
 - Object manipulation: 10 min
 - Balance work: 3x5 min
 - GOAL: Fine motor control

## 💪 Original Program
- Upper Body (2×/week)
 - Push-ups: 3×12
 - Rows: 3×10
 - Press: 3×12
 - GOAL: Functional strength

- Lower Body (2×/week)
 - Squats: 4×15
 - Lunges: 3×12 each
 - Deadlifts: 3×10
 - GOAL: Power base

## 🧘 Recovery Focus
- Cold Exposure
- Meditation
- Fasting
- GOAL: Stress resilience

## 🍽️ Nutrition Approach
### No Sugar Days (5/7)
- Protein: 160g/day
- Veggies: 7-9 servings
- Fruits: 2-3 servings
- GOAL: Clean energy

## 📊 Progress Metrics
- Monday: Weight/mobility
- Friday: Skills check
- Sunday: Recovery assessment
- GOAL: Constant improvement

## 👨‍🏫 Sunday Trainer Review
### 📊 Weekly Metrics
- Weight delta: ±X lbs
- Mobility gains: Y%
- Skill progression: Z/10

### 🎯 Focus Areas
- Stick kata precision
- Kizomba lead refinement
- Stair explosive power
- No-sugar adherence: X/5 days

### 💪 Key Achievements
- Top lift numbers
- Flow state duration
- Recovery quality
- Technical breakthroughs

### 📈 Next Week Targets
- Specific movement patterns
- Nutrition adjustments
- Load progression
- Skill development focus

### 🔄 Program Tweaks
- Volume adjustments
- Intensity modifications
- Recovery protocols
- Nutrition timing
"""

def main():
   st.set_page_config(page_title="Wellness Program", layout="wide")
   
   # Sidebar navigation
   st.sidebar.title("Navigation")
   section = st.sidebar.selectbox(
       "Jump to Section",
       ["Full Program", "Combat Arts", "Dance & Movement", 
        "Dynamic Training", "Precision Work", "Nutrition", 
        "Trainer Review"]
   )
   
   # AI Coach selector
   ai_coach = st.sidebar.selectbox(
       "Select AI Coach",
       ["Movement Coach", "Nutrition Coach", "Recovery Coach", 
        "Combat Arts Coach", "Dance Coach"]
   )
   
   # Print markdown button
   if st.sidebar.button("Print Markdown"):
       st.sidebar.code(WELLNESS_PROGRAM, language="markdown")
   
   # Main content
   st.title("Movement & Wellness Program")
   
   if section == "Full Program":
       st.markdown(WELLNESS_PROGRAM)
   else:
       # Display relevant section (you can add filtering logic here)
       st.markdown(WELLNESS_PROGRAM)
       
   # Coach connection
   if st.sidebar.button("Connect with Coach"):
       st.session_state.coach = ai_coach
       st.success(f"Connected to {ai_coach}")

if __name__ == "__main__":
   main()



# Version 4


# Disciplines I Am Work On:
1. Stress Proofing
2. Shock
3. Fasting
4. Strength
5. Memory
6. Acceptancce

# 🎯 Weekly Fitness Plan

## 💪 Exercise Program
### Original Workouts
- 🏃‍♂️ Running (30min × 3/week)
  - Calories burned: ~300/session
- 🚲 Cycling (45min × 2/week)
  - Calories burned: ~400/session
- 🏊‍♂️ Swimming (30min × 1/week)
  - Calories burned: ~250/session

### Strength Training
- 🏋️‍♀️ Upper Body (2×/week)
  - Push-ups: 3×12
  - Dumbbell rows: 3×10
  - Shoulder press: 3×12
  - Total calories: ~200/session

- 🦵 Lower Body (2×/week)
  - Squats: 4×15
  - Lunges: 3×12 each
  - Deadlifts: 3×10
  - Total calories: ~250/session

## 🍽️ Daily Nutrition
### 📊 Calorie Goals
- 🎯 Daily intake: 2200 cal
- 🔥 Daily burn: 2500 cal
- 📉 Weekly deficit: 2100 cal

### 🥩 Protein Sources (160g/day)
- Chicken breast (30g/4oz)
- Eggs (6g/egg)
- Protein shake (25g/shake)
- Greek yogurt (15g/cup)

### 🥗 Meal Distribution
- Breakfast: 500 cal
- Lunch: 700 cal
- Dinner: 700 cal
- Snacks: 300 cal

## 📅 Weekly Review Notes
- Weight tracked: Monday AM
- Measurements: Friday AM
- Progress photos: Sunday



# Version 3 - AI 

I'll help you create a structured markdown outline with relevant emojis. Let me create a comprehensive outline for your diet and exercise plan.

# 🎯 Fitness and Wellness Plan

## 💪 Exercise Program
### Cardio Workouts
- 🏃‍♂️ Running (30 minutes, 3x/week)
- 🚲 Cycling (45 minutes, 2x/week)
- 🏊‍♂️ Swimming (30 minutes, 1x/week)

### Strength Training
- 🏋️‍♀️ Upper Body
  - 🔨 Push-ups (3 sets of 12)
  - 💪 Dumbbell rows (3 sets of 10)
  - 🏋️ Shoulder press (3 sets of 12)

- 🦵 Lower Body
  - 🏋️‍♂️ Squats (4 sets of 15)
  - 🦿 Lunges (3 sets each leg)
  - 📏 Deadlifts (3 sets of 10)

- 🎯 Core
  - 🔄 Planks (3 sets of 45 seconds)
  - 🌪️ Russian twists (3 sets of 20)
  - 🆙 Crunches (3 sets of 15)

## 🍽️ Nutrition Plan
### 📊 Macro Goals
- 🥩 Protein: 30% of daily calories
- 🥑 Healthy fats: 25% of daily calories
- 🌾 Complex carbs: 45% of daily calories

### 🏪 Grocery List
- 🥩 Proteins
  - 🐔 Chicken breast
  - 🐟 Salmon
  - 🥚 Eggs
  - 🫘 Lentils

- 🥬 Vegetables
  - 🥬 Leafy greens
  - 🥕 Carrots
  - 🥦 Broccoli
  - 🫑 Bell peppers

- 🍎 Fruits
  - 🫐 Berries
  - 🍌 Bananas
  - 🍊 Oranges

## 🛠️ Tools and Equipment
### 🏋️‍♀️ Workout Equipment
- 💪 Dumbbells set
- 🧘‍♀️ Yoga mat
- 📏 Resistance bands
- ⌚ Fitness tracker

### 📱 Apps and Tracking
- 📊 MyFitnessPal (meal tracking)
- ⌚ Strava (cardio tracking)
- 📝 Strong (workout logging)
- ⏰ Interval timer

## 📅 Weekly Schedule
- 🌅 Monday: Upper body + HIIT
- 🏃‍♂️ Tuesday: Cardio
- 💪 Wednesday: Lower body + Core
- 🧘‍♀️ Thursday: Recovery/Yoga
- 🏋️‍♀️ Friday: Full body
- 🚲 Saturday: Cardio + Core
- 😴 Sunday: Rest day


# Version 2 - Prompt:
Help me organize my diet and my workout regimen below to help build out muscle and explosive speed and power for legs and arms, heart & brain health, mental focus, concentration, and organization.
Birth Year: 1971
Gender: Male

# Goals:
Help me blend a two hour brain workout which I do from 4AM - 6AM - at this time I sprint writing AI apps in Python code.
With my brain focus I want to develop better memory, global mindset, and knowledge intake.
Help me blend music I sing, write, dance to and create.  Goal of 10 music videos per week.
Help me develop my artist presence.  Goals of active meaningful reciprocal Social interactions with > 1000 people per day.


# Time Series

1. Monday
2. Tuesday
3. Wednesday
4. Thursday
5. Friday
6. Saturday
7. Sunday

0. Odd Days:
MWF, Sun

1. Even Days:
TTh, Sat

# Tools:
Sauna - 200 degrees
Pool - Cold - 70 (1 swim 2 hour / week 
Pool - Warm - 80
Pool - Sets of pullups on rings
Kenpo Stick Fighting - Two Kata (Continual Speed Attacks both sticks, Block and Tuck Attacks)
Kickboxing
Kizomba Dance 10 minute intervals
High Energy Dance 3 minute intervals
8 lb medicine ball throws, kata while moving, spins, four direction moves
15 lb medicine ball throws, catches, stretches
20 lb shotput
30 lb Kettlebell
Stair Flight Runs Up/Down, Double stairs jumps
Shotput Wing Chun Kata (Continual Speed attacks both arms, asymmetric 5 lbs, 8 lbs).


# Diet
New York Strip + proteins + salad (2 days / week)

Starvation (0 calories) M-F 4AM wake til 1PM.
  Focusing on lifts and energy level to increase alertness, agility, speed, 
  Explosive jumps
  Salads if B needs a boost for energy

Protein and fruit smoothies with Samantha.



# Sets and Exercises:
Breathing practice in Sauna (200 degrees, 5-10 minutes)
Planks (2/week)
Situps (2/week at bedtime)
Crunchies (1 week at bedtime)
Stair Run Jumps (10-20 flights / day, double stair jumps, finish jump)
Outside sprints (3/week short 100m Dash with jumps)
Lifts (2/week Double Water Bottles)








# Time Series

1. Monday
2. Tuesday
3. Wednesday
4. Thursday
5. Friday
6. Saturday
7. Sunday

0. Odd Days:
MWF, Sun

1. Even Days:
TTh, Sat

# Tools:
Sauna - 200 degrees
Pool - Cold - 70 (1 swim 2 hour / week 
Pool - Warm - 80
Pool - Sets of pullups on rings
Kenpo Stick Fighting
20 lb shotput
Stair Flight Runs Up/Down, Double stairs jumps

# Diet
New York Strip + proteins + salad (2 days / week)

Starvation (0 calories) M-F 4AM wake til 1PM.
  Focusing on lifts and energy level to increase alertness, agility, speed, 
  Explosive jumps
  Salads if B needs a boost for energy

Protein and fruit smoothies with Samantha.



# Sets and Exercises:
Breathing practice in Sauna (200 degrees, 5-10 minutes)
Planks (2/week)
Situps (2/week at bedtime)
Crunchies (1 week at bedtime)
Stair Run Jumps (10-20 flights / day, double stair jumps, finish jump)
Outside sprints (3/week short 100m Dash with jumps)
Lifts (2/week Double Water Bottles)
