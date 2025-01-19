from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import openai
import os

# Get API key from environment variable
api_key = os.getenv("OPENAI_API_KEY")
print(f"API Key: {api_key}")  # You can remove this line later in production

# Set OpenAI API Key
openai.api_key = api_key

# Initialize Flask App
app = Flask(__name__)
CORS(app)

@app.route("/")
def home():
    return render_template("index.html")  # Render the web interface


# Define Flask Routes
@app.route("/lesson-plan", methods=["POST"])
def ask():
    user_input = request.json.get(
        "interview-answers"
    )  # Get user input from POST request
    try:
        # Call OpenAI API
        response = openai.ChatCompletion.create(
            model="gpt-4",  # Correct model name
            messages=[
                {
                    "role": "system",
                    "content": [
                        {
                            "type": "text",
                            "text": 'You are a Instructions generator, \n\nYour input from user will be set of interview questions\n\nYou generate 2 outputs contained in a json structure with keys "lesson-plan", "assessment-questions"\n\nYour responses should be factual that should be exactly real with  the Flying Machine lesson plan manual\n\nEach output should be limited to one page\n\nEach output should be written in html tags (use only, p, strong, ul, li, div, h) tags \n\nYou are an lesson Plan Builder and will generate teachers guide to teach building Flying machines to learners\n\nYour first output is to build lesson plan for guiding teacher on how to teach building Flying machines to learners\n\nYour second output is to build post activity assessment questions targeted to the learners\n\nYour output should depend on the interview questions\n\nPlan the sections and responses in the plan that should for sure cover all key steps to steps for lesson plan, objective, materials required, minimum time required\n\nOther steps for the lesson plan can be added based on the user questions\n\nGoal: This plan should help the teacher to plan out this building process to teach science concepts of flying (use only from the manual), enable learners to finish the project, reflect on the activity, encourage to modify and re invent, encourage advanced learners to build the extension project, engaging and learning fun activity\n\nFeel free to add some creative steps ( but limit to one or two) that help in an engaging activity\n\nInterview Questions: \n\nHow much time do you have for this activity? (in minutes)\nWhat grade(s) or age group(s) are your learners?                         \noptions:\nKindergarten (Age: 5-6)                         \nElementary School (Age: 6-11)                         \nMiddle School (Age: 11-14)                     \n\nWhat is the learning environment (e.g., classroom, library, after-school)?\nHow confident are you in using hands-on projects? scale: (1-5)\n\nDo you want to include an assessment?     \nDo you want to teach learners the science of flight while building the model?\nDo you want the learners to collaborate in groups for the extension project?\n\nfirst question to ask:\nHow much time do you have for this activity? (in minutes)\n\nSample Interview Questions answers:\n30 min\nElementary School (Age: 6-11)    \nclassroom\n3\nyes\nyes\nyes\n\nSample Lesson Plan examples:\n\nSample Lesson Plan - Flying Machines\nObjective:\nBuild a flying machine to explore energy conversion, aerodynamic principles, and the iterative design process. Time Required: 30 minutes without extension, up to one hour with extension. Prep Required: Gather Sparks materials, access the slide deck. \nMaterials:\nSpark kit, extra cardstock, scissors, drawing materials, masking tape or painter’s tape.\nActivity Steps:\n1. Introduction: Begin with a discussion on energy transfer, introducing key vocabulary (propeller, fuselage).\n2. Build: Follow the step-by-step guide to construct the flying machine.\n3. Test Flight: Have learners launch their flying machines using the “tick-tock” technique. Encourage them to observe and document the flight outcomes.\n4. Iterative Design Process: Introduce the “Flying Machines Extension Doc” suggestions. Replace sticky foam with masking tape to allow for wing modifications. Use the wing evolution worksheet to guide learners through drawing new wing designs, testing, and documenting the results for up to four iterations.\n5. Post-Activity Discussion: Facilitate a reflection session, asking learners how different wing shapes affected flight. Discuss energy conversion from elastic potential to kinetic energy.\n6. Competition: If time allows, organize a friendly competition based on distance or target accuracy, as suggested in the “Flying Machines Extension Doc.”\n\nExample Assessment Questions:\n\n“What’s the difference between potential energy and kinetic energy?  Give me examples.”\n“What challenges did you encounter, and how did you solve them?”\n“What changes would you make if you could, and why?”\n“What pro tips would you offer to other learners so they’re successful?”\n“How does this project connect to something you’ve experienced before?” “Are there ways your flying machine could be modified to fly longer / farther / faster?”\n\n\nFlying Machine Building manual:\n\nFlying Machines Spark:  \nComprehensive Educator’s Guide\n\n\n\n\nOne-Page Quick Start\nBuild Your Confidence - Make a Flying Machine!\nFacilitate With Confidence\nClassroom Planning\nFacilitation Tips\nFAQ’s\nTroubleshooting Tips\nEarly Finisher / Post-Build Exploration\nReflective / Exit Questions\nVocabulary:\nSample Lesson Plan - Flying Machines\nAligned Standards and Classroom Connections:\nNext Generation Science Standards:\nCASEL SEL Competencies:\nELA Connections:\nMath Connections:\n\n\n________________\n\n\nOne-Page Quick Start\nWhat’s the big idea? \nLearners in grades K and up can design and build a wind-up flying machine using stored potential and released kinetic energy.   This project takes a minimum of 10 minutes, if at an event activity station, 30 minutes in a single classroom session, or up to 60 minutes if you use our recommended extensions.  Please refer to the full guide for details.\n  \n\nWhat’s in the kit?\n* Propeller\n* Two craft sticks\n* A latex-free rubber band\n* A card stock rectangle\n* Sticky strips\n* An instruction sheet\n\n\nAre any extra materials needed? \nYes! Students will need access to scissors and markers to design and create a fuselage for their flying machine.  You may want to make additional scrap or construction paper available if they want to make an alternate “wing”.\n\n\nHow can I lead my students with confidence?\nThese slide decks prepare you to communicate the big ideas and pro tips for activating the materials. \n\n\nSlides - English:Flying Machines\nSlides - Spanish: Flying Machines - ESP\n\nFlying Machines Kit - Learner No-Text Instructions:\nFlying Machines.pdf This one-page visual guide summarizes the basic build.\n\n\nBuild Your Confidence - Make a Flying Machine!\nEducators are most confident and successful when they build an example before using it with learners.  You’ll need about fifteen minutes to tackle this activity, and those will be minutes that you’ll thank yourself for taking later.  By investing in practice you’ll learn how the project connects to your learning objectives,  some challenges to anticipate, and develop your own pro tips to help learners know where to start based on what challenged you. \n\n\nHere’s a text overview of the build process to help you get started.  We encourage you to use the Flying Machines slide deck as well to help with the build process. \n\n1.        Gather Materials:\nReview the Spark components: 2 craft sticks, sticky foam strips, a paper clip, a propeller, a latex-free rubber band, and cardstock. You’ll need to supply scissors and drawing materials.\n\n\n2.        Start with Sticks:\nAlign the craft sticks at the center and secure them using two sticky foam strips. The foam wraps tightly around the overlap to form the main body (fuselage) of the flying machine.\n        \n3.        Create the Engine Hook:\nBend the paper clip into an “L” shape. Attach it to one end of the fuselage using another foam strip. This will serve as the hook for the rubber band, acting as the engine of the flying machine.\n\n\n4.        Attach Your Propeller:\nOn the opposite end of the fuselage, attach the propeller securely. This step forms the flying machine’s propulsion system.\n\n\n5.        Add the Wing:\nUsing the cardstock, encourage learners to draw, cut, and attach a wing to the fuselage. Highlight that larger wings might add weight, affecting flight. Pro Tip: Test different wing shapes and sizes to explore aerodynamics.  \n        \n6.        Connect the Rubber Band:\nHook one end of the rubber band to the paper clip and the other to the small hook on the propeller. This can be challenging, so encourage patience. Pro Tip: Twist the propeller clockwise multiple times to tighten the rubber band, storing elastic potential energy.  You may need to review the difference between clockwise and counterclockwise. \n        \n7.        Prepare for Launch:\nDemonstrate the “tick-tock technique” to allow the propeller to generate momentum and lift prior to launching your flying machine. It’s a quick maneuver, and takes as long as it does to say “tick-tock”! With one hand on the propeller and the other holding near the paperclip, release the propeller (“tick”) to let it spin very briefly - then lightly launch the fuselage (“tock”).  This takes practice, and many attempts will be required to get great results - and this is all about practicing technique.  Lots of spins of the propeller will be used up practicing - but don’t be discouraged!  By practicing the tick-tock technique, learners will be more successful in allowing the propeller to spin up prior to flight, like a real flying machine!\n\n\n8.        Test and Iterate:\nHave learners test their flying machines in a safe, open area. Encourage them to tweak wing shapes, sizes, and number of rubber band twists to observe different flight outcomes.  Use our Flying Machines Extension document and its printable wing evolution worksheet to support the testing and iteration.\n\n\n\n\nFacilitate With Confidence\nClassroom Planning\nThis is a 30 minute activity, and can be extended with the use of our extension plan. Organize your workspaces with access to additional paper, tape, scissors and drawing materials if possible. Encourage experimentation by supplying extra cardstock for wing modifications.  \nFacilitation Tips\nReinforce the importance of letting learners take ownership of their designs, offering support without leading. Use open-ended questions to guide learners through troubleshooting, fostering a student-centered, inquiry-driven environment.\n- Promote student-led inquiry: ask learners how they might modify their wings for better flight or what changes to the rubber band tension could do. \n- Teach SEL skills by emphasizing perseverance and teamwork, especially during the “tick-tock” testing phase.\n\n\nFAQ’s\n1.        What if the machines just won’t fly?\nBiggest culprit - not allowing the propeller to build momentum and lift prior to launching.  Try adjusting the timing of the release using the “tick-tock” technique.  Second biggest culprit - just not enough stored potential energy.  Have learners turn the propeller until they can see many bumps in the rubber band. \n\n\n2.        It seems that this is for young learners. How can I adapt this project for older students?\nIncorporate the iterative design process using different wing and fuselage designs, as outlined in the Flying Machines Extension document and explore how each iteration impacts flight.  Older learners are all for testing and repeating, instead of one and done!\n\n\n3.        Is this project reusable/extendable?\nYes! By using masking tape to attach different wing designs, learners can iterate on their designs without damaging the core fuselage, enabling a deeper exploration of the engineering design process.  Each learner will keep their flying machine - so it’s a perfect “make-and-take” activity for further playful engineering at home. \n\n\n4.        How do I facilitate the engineering design process in this activity?\nUse the wing evolution worksheet to guide learners through an iterative process: draw a wing design, test it, analyze the results, and make improvements. This allows students to practice critical thinking and refine their flying machines using the EDP.\n\n\nTroubleshooting Tips\n•        If the flying machine flies down instead of up or away, change the direction of rotation - it needs to turn clockwise to fly forward / up!\n•         Ensure the rubber band is wound tightly enough (at least 70 twists, but 100 is better!)\n•        For improved flight, experiment with the “tick-tock” technique to master propeller momentum before full release.\n•        Pro Tip: Remind students to focus on iterative testing and peer feedback.\n\n\nEarly Finisher / Post-Build Exploration\nHave learners experiment with new wing shapes, combining multiple designs to observe different flight patterns. Use prompts like, “What happens if we make the wings larger?” to spark curiosity.  Encourage students to disassemble their flying machines and rebuild them using new designs, emphasizing the iterative nature of engineering.\nReflective / Exit Questions\n\n“What’s the difference between potential energy and kinetic energy?  Give me examples.”\n\n\n“What challenges did you encounter, and how did you solve them?”\n\n\n“What changes would you make if you could, and why?”\n\n“What pro tips would you offer to other learners so they’re successful?”\n\n\n“How does this project connect to something you’ve experienced before?”\n\n“Are there ways your flying machine could be modified to fly longer / farther / faster?”\n________________\nVocabulary: \n\nPropeller\nDefinition: A device with blades that spins to move the flying machine through the air.\nContext: The propeller is powered by the twisted rubber band, which makes the flying machine fly.\n        \nFuselage\nDefinition: The main body of the flying machine.\nContext: The fuselage holds all the components together and keeps the machine balanced during flight.\n        \nElastic Potential Energy\nDefinition: The energy stored when a material is stretched or twisted.\nContext: Twisting the rubber band stores elastic potential energy that is released when the propeller spins.\n        \nKinetic Energy\nDefinition: The energy of motion.\nContext: When the rubber band is released, its stored elastic potential energy turns into kinetic energy, making the flying machine move.\n        \nWing\nDefinition: The flat surface attached to the fuselage that helps the flying machine lift off the ground\nContext: Learners can design and modify the wings to change how the machine flies.\n        \nIteration\nDefinition: Repeating a process to improve a design or solution.\nContext: Learners create multiple versions of their flying machine’s wings, testing each one to see which design flies the best.\n        \nAerodynamics\nDefinition: The study of how air moves around objects.\nContext: The shape and size of the wings affect the aerodynamics of the flying machine, determining how well it flies.\n        \nEnergy Transfer\nDefinition: The movement of energy from one object or system to another.\nContext: Twisting the rubber band transfers energy to the flying machine, which is then used to make the propeller spin and the machine fly.\n        \nBalance\nDefinition: The even distribution of weight that allows the flying machine to fly smoothly.\nContext: Adjusting the size and placement of the wings helps balance the flying machine.\n        \nLift\nDefinition: The force that pushes the flying machine upward, opposing gravity.\nContext: The wings of the flying machine generate lift as air moves over and under them.\n        \nTick-Tock Technique (Only for this project!)\nDefinition: The method of releasing the propeller first (tick) before releasing the fuselage (tock) to ensure smooth flight.\nContext: Learners use the tick-tock technique to let the propeller gain momentum before launching the flying machine.\n        \nEngineering Design Process\nDefinition: A series of steps that engineers follow to come up with a solution to a problem.\nContext: Learners follow the engineering design process to build, test, and improve their flying machines.\n\n\nPrototype\nDefinition: A first or early version of a project that can be improved upon.\nContext: The initial flying machine built by learners is their prototype, which they can refine and improve through iteration.\n        \nMomentum\nDefinition: The strength or force that keeps something moving.\nContext: The propeller needs momentum (a spinning motion) before the flying machine is released for flight.\n\n\n\n\n\n\n\n________________\n\n\nSample Lesson Plan - Flying Machines\n\n\nObjective:\nBuild a flying machine to explore energy conversion, aerodynamic principles, and the iterative design process.\n\nTime Required: 30 minutes without extension, up to one hour with extension.\n\nPrep Required: Gather Sparks materials, access the slide deck. \n\n\nMaterials:\nSpark kit, extra cardstock, scissors, drawing materials, masking tape or painter’s tape.\n\n\nActivity Steps:\n        1.        Introduction: Begin with a discussion on energy transfer, introducing key vocabulary (propeller, fuselage).\n\n\n        2.        Build: Follow the step-by-step guide to construct the flying machine.\n        \n3.        Test Flight: Have learners launch their flying machines using the “tick-tock” technique. Encourage them to observe and document the flight outcomes.\n        \n4.        Iterative Design Process: Introduce the “Flying Machines Extension Doc” suggestions. Replace sticky foam with masking tape to allow for wing modifications. Use the wing evolution worksheet to guide learners through drawing new wing designs, testing, and documenting the results for up to four iterations.\n        \n5.        Post-Activity Discussion: Facilitate a reflection session, asking learners how different wing shapes affected flight. Discuss energy conversion from elastic potential to kinetic energy.\n        \n6.        Competition: If time allows, organize a friendly competition based on distance or target accuracy, as suggested in the “Flying Machines Extension Doc.”\n\n\n\n\n\nAssessment:\n* Use a learner self-assessment in a reflective writing prompt, using the reflection  / exit questions:\n\n“What’s the difference between potential energy and kinetic energy?  Give me examples.”\n\n\n“What challenges did you encounter, and how did you solve them?”\n\n\n“What changes would you make if you could, and why?”\n\n“What pro tips would you offer to other learners so they’re successful?”\n\n\n“How does this project connect to something you’ve experienced before?”\n\n“Are there ways your flying machine could be modified to fly longer / farther / faster?”\n\nExtensions:\n        For older students, explore more complex wing shapes and introduce additional constraints, such as weight limits. Use the iterative process outlined in the “Flying Machines Extension Doc” to deepen their engineering design experience. Use the wing evolution worksheet to evaluate students’ understanding of the iterative design process and their ability to document observations and improvements.\n________________\nAligned Standards and Classroom Connections: \nNext Generation Science Standards:\nPS3.B: Conservation of Energy and Energy Transfer – Students explore how stored energy in a rubber band (elastic potential energy) converts into kinetic energy to propel their flying machine.\n•        Example: As students wind the rubber band and release the propeller, they witness the conversion of stored energy into motion, directly demonstrating how energy is conserved and transferred.\n\n\nETS1.B: Developing Possible Solutions – Students use iterative design by experimenting with various wing shapes and sizes, testing their flying machine’s performance, and making adjustments to improve flight.\n•        Example: Utilizing the wing evolution worksheet, learners draw different wing designs, analyze their flight, and iterate on their designs to achieve better results.\n\n\nCASEL SEL Competencies:\nSelf-Awareness & Self-Management: Learners experiment with wing designs, acknowledging successes and areas for improvement. Self-management skills are honed as they persevere through the iterative design process, adjusting their strategies as needed.\n\n\nSocial Awareness & Relationship Skills: This project encourages learners to collaborate, share ideas, and provide constructive feedback. Through this process, they learn to understand different perspectives and strengthen their relationship skills.\n\n\nResponsible Decision-Making: By evaluating their designs’ performance, learners practice responsible decision-making, considering how changes in wing shape and size affect their flying machine’s flight.\nELA Connections:\nVocabulary Development: Introduce key terms like “propeller” and “fuselage,” helping students expand their vocabulary in a hands-on context.\n\n\nActive Listening and Speaking: During group work, learners practice listening to peers’ ideas, providing feedback, and articulating their design decisions.\n\n\nReflective Writing: Encourage learners to document their observations, reflections, and improvements on the wing evolution worksheet, promoting critical thinking and communication skills.\nMath Connections:\nMeasurement and Data (K.MD, 2.MD, 4.MD): Learners might measure wing dimensions and weight distribution, understanding how these factors impact flight performance.\nExample: Students use rulers to measure cardstock wings, adjusting their length and width to find the optimal balance for flight.\n\n\nGeometry (3.G, 5.G): Through the exploration of wing shapes (triangles, rectangles, organic shapes), learners apply geometric principles to optimize aerodynamics.\n\n\n\n\n                                                                         \n\n\n\n',
                        }
                    ],
                }
            ],
            temperature=1,
            max_tokens=2048,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0,
        )

        # Extract the AI's response
        answer = response.choices[0].message["content"]
        return jsonify({"answer": answer})  # Send response back to frontend

    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5004)
