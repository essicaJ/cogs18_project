class MajorInfo():
    
    """The following class is used to organize some basic information about different psycholoyg majors,
    and return answer with the specific information according to user's input.
        
    Attributes
    ----------   
    name(str): the name of the specialization
    code(str): the major code of the specialization
    summary(str): brief summary of the major's focus
    
    """
    def __init__(self, name, code, summ):
        """
        parameters
        ----------
        name(str): the name of the specialization
        code(str): the major code of the specialization
        summary(str): brief summary of the major's focus
        
        """
        
        self.name = name
        self.code = code
        self.summ = summ
        
    def name_func(self):
        """This method print chatbot output about major's name"""
        return('The major your are asking about is' + ': '+ self.name)

    def code_func(self):
        """This method print chatbot output about major's code"""
        return('The code of the the major your are asking about is' + ': ' + self.code)

    def summary_func(self):
        """This method print chatbot output about major's summary"""
        return('The description of this major is' + ': ' + self.summ)
    
    def all_info_func(self):
        """This method print chatbot output about major's name, code and summary"""
        return(self.name + ' ' + self.code + ': ' + self.summ)

"""The following dictionary stores major information by calling on above class.
   It also allows the chatbot to return the information(stored as dic value), when user inputs the key that matches it."""

information = {'Psychology': MajorInfo('Psychology B.S.', 'PC26', 
                                       'The B.S. in Psychology is designed to provide broad knowledge' +\
                                       'across sub-disciplines in Psychology' +\
                                       'With an emphasis on statistics and research methods,' +\
                                       'this major includes a research requirement that' +\
                                       'can be satisfied through independent research or lab classes. '),
              'Business Psychology': MajorInfo('Business Psychology B.S.', 'PC35',
                                               'The Business Psychology major is designed' +\
                                               'to train students to apply psychological principles' +\
                                               'to the workplace and to organizational challenges and opportunities therein.'),
              'Clinical Psychology': MajorInfo('Psychology B.S. with a Specialization in Clinical Psychology', 'PC28',
                                               'The Clinical Psychology specialization provides'+\
                                               'instruction in the psychological and physiological' +\
                                               'causes of and treatments for mental illness in children and adults.'),
              'Cognitive Psychology': MajorInfo('Psychology B.S. with a Specialization in Cognitive Psychology', 'PC29',
                                                'Cognitive Psychology includes understanding'+\
                                                'reasoning, thinking, language, judgment,' +\
                                                'and decision making in adults and children' +\
                                                '(including attention, memory, and visual and auditory information processing.)'),
              'Developmental Psychology': MajorInfo('Psychology B.S. with a Specialization in Developmental Psychology', 'PC30',
                                                'Developmental Psychology entails all aspects' +\
                                                'of human development with emphases on social and personality' +\
                                                'development, perceptual development, and language acquisition.' +\
                                                'This specialization also includes the study of developmental psychopathology.'),
              'Human Health Psychology': MajorInfo('Psychology B.S. with a Specialization in Human Health', 'PC31',
                                                   'Health psychology focuses on understanding' +\
                                                   'how psychological, biological, and environmental factors' +\
                                                   'interact to jointly influence human health. Topics include' +\
                                                   'addiction, impulsive behavior, and issues related to cognitive control.'),
              'Sensation Perception Psychology': MajorInfo('Psychology B.S. with a Specialization in Sensation and Perception', 'PC32',
                                                           'Sensation and Perception is the study of how our sense organs and brain'+\
                                                           'allow us to construct' +\
                                                           'our consciously experienced representation of the environment.'+\
                                                           'Experiments using computer-controlled' +\
                                                           'stimuli are used to test models of sensory or perceptual processes.' +\
                                                           'Processes of particular interest include color vision, motion perception,'+\
                                                           'and auditory illusions and paradoxes.'),
              'Social Psychology': MajorInfo('Psychology B.S. with a Specialization in Social Psychology', 'PC33',
                                             'Social Psychology is the study of human behavior in social situations.' +\
                                             'The specialization focuses on topics including emotion, aggression,'+\
                                             'and social cognition. It also encompasses applied social psychology,' +\
                                             'including psychology and the law and behavioral medicine.'),
              'Cognitive Bahavioral Neuroscience': MajorInfo('Cognitive and Behavioral Neuroscience B.S.', 'PC34',
                                                            'Cognitive and Behavioral Neuroscience is a joint major between the' +\
                                                            'Department of Cognitive Science and the Department of Psychology.' +\
                                                             'Students may choose to be advised by either department.'+\
                                                            'The B.S. in Cognitive and Behavioral Neuroscience will appeal' +\
                                                             'to students who are broadly interested in understanding links between' +\
                                                            'neural activity and perception (e.g., color vision, attention),' +\
                                                             'basic behaviors (e.g., appetitive drives), and higher' +\
                                                             'level cognitive function' +\
                                                             '(e.g., working memory and executive function) using multiple tools' +\
                                                             'ranging from single-unit physiology to functional magnetic resonance' +\
                                                             'imaging (fMRI) and electroencephalography (EEG).')}

# I choose to organize the lower division requirements of each major with a dictionary of dictionaries, with each each 'small' dictionaries containing specific requirement and courses that satisfy it,
# This allows me to pair each major with its requirements and get courses that satisfy the requirements for the chatbot function
req_natural_science = {'Natural Sciences': ['BILD 1', 'BILD 2', 'BILD 3', 'BILD 10', 'BILD 12', 'BILD 20', 
                      'BILD 26', 'CHEM 4', 'CHEM 6A', 'CHEM 6B', 'CHEM 6C', 'CHEM 11', 'CHEM 12', 'CHEM 13',
                      'COGS 17', 'PHYS 1A', 'PHYS 1B', 'PHYS 1C', 'PHYS 2A', 'PHYS 2B', 'PHYS 2C', 'PHYS 10', 'PHYS 11', 'PSYC 2']}

req_formal_skills = {'Formal Skills':['MATH 10A', 'MATH 20A', 'MATH 10B', 'MATH 20B', 'PSYC 70']}

req_computer_programming = {'Computer Programming': ['CSE 5A', 'CSE 7', 'CSE 8A', 'CSE 8B', 'CSE 11', 
                                                    'CSE 12', 'COGS 18', 'ECE 15', 'MAE 5', 'MAE 8']}

req_statistics = {'Statistics': ['PSYC 60', 'BENG 100', 'BIEB 100', 'COGS 14B', 'ECON 120A', 'MATH 11', 
                                 'MATH 181A', 'MATH 183', 'MATH 186']}
req_business = {'business' : ['MGT 16', 'MGT 18']}

req_upper_core = {'upper division Core': ['PSYC 100', 'PSYC 101', 'PSYC 102', 'PSYC 104', 'PSYC 105', 'PSYC 106', 'PSYC 108']}

req_additional_upper = {'additional upper courses': ['PSYC 100 - 193']}

req_business_upper = {'Business Courses': ['MGT 103', 'MGT 105', 'MGT 106', 'MGT 129', 'MGT 154', 'MGT 162', 'MGT 164']}

req_clinical_upper_specialization = {'Upper Clinical Specialization': ['PSYC 116', 'PSYC 124', 'PSYC 125',
                                                                       'PSYC 132', 'PSYC 133', 'PSYC 134', 'PSYC 151', 
                                                                       'PSYC 154', 'PSYC 155', 'PSYC 168', 'PSYC 172',
                                                                       'PSYC 184', 'PSYC 188', 'PSYC 190']}

req_cognitive_upper_specialization = {'Upper Cognitive Specialization': ['PSYC 114', 'PSYC 115A', 'PSYC 115B', 
                                                                         'PSYC 123', 'PSYC 128', 'PSYC 129', 'PSYC 137', 
                                                                         'PSYC 141', 'PSYC 142', 'PSYC 144', 'PSYC 145',
                                                                         'PSYC 146', 'PSYC 148', 'PSYC 152', 'PSYC 156', 
                                                                         'PSYC 161', 'PSYC 170', 'PSYC 171', 'PSYC 174',
                                                                         'PSYC 176', 'PSYC 187', 'PSYC 191']}
req_developmental_upper_specialization = {'Upper Cognitive Specialization': ['PSYC 136', 'PSYC 146', 'PSYC 147',
                                                                             'PSYC 152', 'PSYC 156', 'PSYC 158', 'PSYC 168',
                                                                             'PSYC 172', 'PSYC 180', 'PSYC 187', 'PSYC 190']}
req_human_health_upper_specialization = {'Upper Human Health Specialization': ['PSYC 123', 'PSYC 124', 'PSYC 130',
                                                                               'PSYC 132', 'PSYC 133', 'PSYC 134', 'PSYC 154',
                                                                               'PSYC 155', 'PSYC 168', 'PSYC 169', 'PSYC 171',
                                                                               'PSYC 172', 'PSYC 179', 'PSYC 181', 'PSYC 184',
                                                                               'PSYC 188', 'PSYC 191']}
req_sensation_perception_upper_specialization = {'Upper Sensation Perception Specialization': ['PSYC 123', 'PSYC 124', 'PSYC 130',
                                                                                               'PSYC 132', 'PSYC 133', 'PSYC 134', 
                                                                                               'PSYC 154', 'PSYC 155', 'PSYC 168',
                                                                                               'PSYC 169', 'PSYC 171', 'PSYC 172',
                                                                                               'PSYC 179', 'PSYC 181', 'PSYC 184',
                                                                                               'PSYC 188', 'PSYC 191']}
req_social_specialization = {'Upper Social Specialization': ['PSYC 114', 'PSYC 130', 'PSYC 137', 'PSYC 139', 'PSYC 141',
                                                             'PSYC 147', 'PSYC 152', 'PSYC 153', 'PSYC 155', 
                                                             'PSYC 157', 'PSYC 158', 'PSYC 162', 'PSYC 164', 
                                                             'PSYC 172', 'PSYC 176', 'PSYC 178', 'PSYC 187', 'PSYC 190']}

req_cognitive_behavioral_neuroscience = {'Upper Cognitive Behavioral Neuroscience': ['PSYC 116', 'PSYC 122', 'PSYC 123',
                                                                                     'PSYC 125', 'PSYC 132', 'PSYC 133',
                                                                                     'PSYC 144', 'PSYC 150', 'PSYC 159', 'PSYC 169',
                                                                                     'PSYC 170', 'PSYC 171', 'PSYC 179', 'PSYC 181',
                                                                                     'PSYC 189',
                                                                                     'COGS 115', 'COGS 119', 'COGS 154',
                                                                                     'COGS 163', 'COGS 164', 'COGS 169', 'COGS 171',
                                                                                     'COGS 172', 'COGS 174', 
                                                                                     'COGS 175', 'COGS 176', 'COGS 177',
                                                                                     'COGS 178', 'COGS 179', 'COGS 180',
                                                                                     'COGS 184', 'HDP 110']}

req_research = {'research requirement': ['PSYC 71', 'PSYC 81', 'PSYC 99', 'PSYC 114', 'PSYC 115A',
                                         'PSYC 115B', 'PSYC 116', 'PSYC 117', 'PSYC 121', 'PSYC 140',
                                         'PSYC 193L', 'PSYC 194A', 'PSYC 194B', 'PSYC194C', 'PSYC 199']}

req_research_busi = {'Business Psych Research' : ['MGT 52', 'MGT 153', 'PSYC 199', 'MGT 199',
                                                  'PSYC 194A', 'PSYC 194B', 'PSYC194C', 'PSYC 199']}


class MajorRequirement():
    """The following class is used to organize lower and upper requirement courses about different psycholoyg majors,
    and return answer with the information according to user's input.
        
    Attributes
    ----------   
    lower_req(list): a list of dictionaries that store lower division courses as strings 
    upper_req(list): a list of dictionaries that store upper division courses as strings
    
    """
    
    def __init__(self, lower_req, upper_req):
        """
        parameters
        ----------
        lower_req(list): a list of dictionaries that store lower division courses as strings 
        upper_req(list): a list of dictionaries that store upper division courses as strings
        
        """
        self.lower_req = lower_req
        self.upper_req = upper_req
    
    def lower_courses(self):
        """This method print chatbot output about major's lower division requirement courses"""
        return('Here are the lower requirement courses' + ': ' + str(self.lower_req))
        
    def upper_courses(self):
        """This method print chatbot output about major's upper division requirement courses"""
        return('Here are the upper requirement courses' + ': ' + str(self.upper_req))
    

"""The following dictionary stores major information by calling on above class.
   It also allows the chatbot to return the information(stored as dic value), when user inputs the key that matches it."""
courses = {'Psychology Courses': MajorRequirement([req_natural_science, req_formal_skills, req_computer_programming, req_statistics],
                                                  [req_upper_core, req_additional_upper]),
           'Business Psychology Courses': MajorRequirement([req_natural_science, req_formal_skills,
                                                            req_computer_programming, req_statistics, req_business],
                                                           [req_upper_core, req_additional_upper, req_business_upper]),
           'Clinical Psychology Courses': MajorRequirement([req_natural_science, req_formal_skills,
                                                            req_computer_programming, req_statistics],
                                                         [req_upper_core, req_additional_upper, req_clinical_upper_specialization]),
           'Cognitive Psychology Courses': MajorRequirement([req_natural_science, req_formal_skills,
                                                             req_computer_programming, req_statistics],
                                                            [req_upper_core, req_additional_upper,
                                                             req_cognitive_upper_specialization]),
           'Developmental Psychology Courses': MajorRequirement([req_natural_science, req_formal_skills,
                                                                 req_computer_programming, req_statistics],
                                                              [req_upper_core, 
                                                               req_additional_upper, req_developmental_upper_specialization]),
           'Human Health Psychology Courses': MajorRequirement([req_natural_science, 
                                                                req_formal_skills, req_computer_programming, req_statistics],
                                                             [req_upper_core,
                                                              req_additional_upper, req_human_health_upper_specialization]),
           'Sensation Perception Psychology': MajorRequirement([req_natural_science, 
                                                                req_formal_skills, req_computer_programming, req_statistics],
                                                             [req_upper_core,
                                                              req_additional_upper, req_sensation_perception_upper_specialization]),
           'Social Psychology': MajorRequirement([req_natural_science, req_formal_skills, req_computer_programming, req_statistics],
                                               [req_upper_core, req_additional_upper, req_social_specialization]),
           'Cognitive Behavioral Psychology': MajorRequirement([req_natural_science, req_formal_skills,
                                                                req_computer_programming, req_statistics],
                                                             [req_upper_core, 
                                                              req_additional_upper, req_cognitive_behavioral_neuroscience])}
def talk_psych():
    "Main function for chatbot"
    
    chat = True
    print('Welcome to Psychology Majors Chatbot! Here you can find all information you want for UCSD Psych majors! \n'
             'What do you want to know? \n' +
             "Start by typing in 'Psychology', 'Business Psychology', 'Clinical Psychology', 'Cognitive Psychology'," +\
              "'Developmental Psychology', 'Human Health Psychology', 'Sensation Perception Psychology'," +\
              "'Social Psychology', or 'Cognitive Behavioral Neuroscience'. \n" +
             "if instead, you want course requirements of specific major, type in 'major name + courses'. \n" +
             "Type 'quit', 'bye', or 'ok' to exit.")
    
    while chat:# loop through all possible output using user's input and return appropriate output until user input that exit the loop.
        
        user_msg = input('INPUT :\t') # Get User's input
        
        if user_msg in information.keys(): # Check if user is asking about major information, 
                                           # and return specific information: name, code, summary, or all.
            print("What information would you like to hear about this major? Type 'name', 'code', 'summary', or 'all'!")
            
            while True: # Use another while loop so user can decide to keep checking major information or start over.
                user_msg2 = input('INPUT :\t') # Get users' new input about specific information 
            
                # These code run the method created in class according to user's input.
                if user_msg2 == 'name':
                    information.get(user_msg).name_func()
                elif user_msg2 == 'code':
                    information.get(user_msg).code_func()
                elif user_msg2 == 'summary':
                    print('Here is what it does')
                    information.get(user_msg).summary_func()
                elif user_msg2 == 'all':
                    print('Here is all of it!')
                    information.get(user_msg).all_info_func()
                else:
                    print("Sorry, I do not understand. Please type 'name', 'code', 'summary', or 'all'.")
                
                #The following code allows user to choose to continue or start over.
                print("what other information do you want? Type 'quit' to start over or 'continue' to look up another major.")
                user_msg3 = input('INPUT :\t')
                if user_msg3 == 'quit':
                    print("start again by typing in major name or major name + 'Courses' for course requirement!")
                    break  
                elif user_msg3 == 'continue':
                    print("Type in name of another major for its major information.")
                    break
                      
        elif user_msg in courses.keys(): # Check if user is asking about course requirements, 
                                         # and return specific information: lower, upper, or all requirements.             
            print("What requirement would you like to hear about this major? Type 'lower' or 'upper'!")
            
            while True: # Use another while loop so user can decide to keep checking course requirement or start over.
                user_msg4 = input('INPUT :\t')
                
                # These code run the method created in class according to user's input.
                if user_msg4 == 'lower':
                    print('Here are all lower requirement courses for this major!')
                    print(courses.get(user_msg).lower_req)
                elif user_msg4 == 'upper':
                    print('Here are all upper requirement courses! for this major!')
                    print(courses.get(user_msg).upper_req)
                else:
                    print("Sorry, I do not understand. Please type 'lower' or 'upper'.")
                
                # The following code allows user to choose to continue or start over.
                print("what other information do you want? Type 'quit' or continue.")
                user_msg5 = input('INPUT :\t')
                if user_msg5 == 'quit':
                    print("start again by typing in major name or major name + 'Courses' for course requirement!")
                    break
                elif user_msg5 == 'continue':
                    print("Type in name of another major + courses for its course requirement.")
                    break
        
        # These code exit the loop if user choose to.
        elif 'quit' or 'bye' or 'ok' in user_msg:
            print('Bye! Have a nice day!')
            chat = False

        else:
            print('I do not understand.')