#Personal Questions
INSERT INTO questions (question_text, person) VALUES ('What is your firstname?', 'advantage');
INSERT INTO questions (question_text, person) VALUES ('What is your secondname?', 'advantage');
INSERT INTO questions (question_text, person) VALUES ('What did you study?', 'advantage');
INSERT INTO questions (question_text, person) VALUES ('What is your current job?', 'advantage');

#General Desktop vs Laptop Questions
INSERT INTO questions (question_text, category) VALUES ('Why would you choose a desktop over a laptop?', 'advantage');
INSERT INTO questions (question_text, category) VALUES ('What are the disadvantages of using a desktop?', 'disadvantage');

#Device Usage
INSERT INTO questions (question_text, category) VALUES ('What do you primarily use your computer for?', 'Usage');
INSERT INTO questions (question_text, category) VALUES ('How many hours a day do you use your computer?', 'Usage');
INSERT INTO questions (question_text, category) VALUES ('Do you require specific software that performs better on a desktop than on a laptop?', 'Usage');

#Cost
INSERT INTO questions (question_text, category) VALUES ('What is your budget for a computer?', 'Cost');
INSERT INTO questions (question_text, category) VALUES ('Do you think a desktop is more cost-efficient than a laptop in the long run?', 'Cost');

#External Devices
INSERT INTO questions (question_text, category) VALUES ('Do you use an external keyboard with your current device?', 'External Devices');
INSERT INTO questions (question_text, category) VALUES ('Do you use an external monitor with your current device?', 'External Devices');
INSERT INTO questions (question_text, category) VALUES ('How important is ergonomics to you?', 'External Devices');

#Mobility and Usability
INSERT INTO questions (question_text, category) VALUES ('How important is portability in a computer for you?', 'Mobility');
INSERT INTO questions (question_text, category) VALUES ('Do you often need to use your computer in different locations?', 'Mobility');
INSERT INTO questions (question_text, category) VALUES ('Would you prefer your computer to always stay in one fixed location?', 'Mobility');

#Performance and Expandability
INSERT INTO questions (question_text, category) VALUES ('How important is the ability to upgrade your device in the future?', 'Performance');
INSERT INTO questions (question_text, category) VALUES ('Which components do you consider most important for good performance?', 'Performance');
