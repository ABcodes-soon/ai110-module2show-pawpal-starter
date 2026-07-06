import streamlit as st

from pawpal_system import Owner, Pet, Scheduler, Task

st.set_page_config(page_title="PawPal+", page_icon="🐾", layout="centered")

st.title("🐾 PawPal+")

st.markdown(
    """
Welcome to the PawPal+ starter app.

This file is intentionally thin. It gives you a working Streamlit app so you can start quickly,
but **it does not implement the project logic**. Your job is to design the system and build it.

Use this app as your interactive demo once your backend classes/functions exist.
"""
)

with st.expander("Scenario", expanded=True):
    st.markdown(
        """
**PawPal+** is a pet care planning assistant. It helps a pet owner plan care tasks
for their pet(s) based on constraints like time, priority, and preferences.

You will design and implement the scheduling logic and connect it to this Streamlit UI.
"""
    )

with st.expander("What you need to build", expanded=True):
    st.markdown(
        """
At minimum, your system should:
- Represent pet care tasks (what needs to happen, how long it takes, priority)
- Represent the pet and the owner (basic info and preferences)
- Build a plan/schedule for a day that chooses and orders tasks based on constraints
- Explain the plan (why each task was chosen and when it happens)
"""
    )

st.divider()

st.subheader("Quick Demo Inputs")

if "owner" not in st.session_state:
    st.session_state.owner = Owner(name="Jordan")
if "pet" not in st.session_state:
    st.session_state.pet = Pet(name="Mochi", species="dog")

owner = st.session_state.owner
pet = st.session_state.pet

if pet not in owner.pets:
    owner.add_pet(pet)

with st.expander("Add another pet", expanded=False):
    new_pet_name = st.text_input("New pet name", key="new_pet_name")
    new_pet_species = st.selectbox("New pet species", ["dog", "cat", "other"], key="new_pet_species")
    if st.button("Add pet"):
        if new_pet_name.strip():
            new_pet = Pet(name=new_pet_name.strip(), species=new_pet_species)
            owner.add_pet(new_pet)
            st.session_state.pet = new_pet
            pet = st.session_state.pet
            st.success(f"Added {pet.name} to your pets.")
        else:
            st.warning("Please enter a pet name.")

st.write("Current pets:")
for current_pet in owner.pets:
    st.write(f"- {current_pet.name} ({current_pet.species})")

owner_name = st.text_input("Owner name", value=owner.name)
pet_name = st.text_input("Pet name", value=pet.name)
species_options = ["dog", "cat", "other"]
species_index = species_options.index(pet.species) if pet.species in species_options else 0
species = st.selectbox("Species", species_options, index=species_index)

owner.name = owner_name
pet.name = pet_name
pet.species = species

st.markdown("### Tasks")
st.caption("Add a few tasks. These are stored in the live session state and used by the scheduler.")

col1, col2, col3 = st.columns(3)
with col1:
    task_title = st.text_input("Task title", value="Morning walk")
with col2:
    duration = st.number_input("Duration (minutes)", min_value=1, max_value=240, value=20)
with col3:
    priority = st.selectbox("Priority", ["low", "medium", "high"], index=2)

if st.button("Add task"):
    task = Task(title=task_title, duration_minutes=int(duration), priority=priority)
    pet.add_task(task)

if pet.tasks:
    st.write("Current tasks:")
    task_rows = [
        {"title": task.title, "duration_minutes": task.duration_minutes, "priority": task.priority}
        for task in pet.tasks
    ]
    st.table(task_rows)
else:
    st.info("No tasks yet. Add one above.")

st.divider()

st.subheader("Build Schedule")
st.caption("This button uses the stored owner and pet state to generate a schedule.")

if st.button("Generate schedule"):
    scheduler = Scheduler(available_time_minutes=60)
    plan = scheduler.generate_daily_plan(owner)

    if plan:
        st.success("Scheduled tasks:")
        for index, task in enumerate(plan, start=1):
            st.write(f"{index}. {task.title} ({task.duration_minutes} min, {task.priority})")
        st.caption(scheduler.explain_plan(owner))
    else:
        st.info("No tasks fit into the available time.")
