"""Subclass of Listbox, which is generated by wxFormBuilder."""

import wx
import AppsSDS.temp as temp

# Implementing Listbox
class TempListbox( temp.Listbox1 ):
	def __init__( self,parent ):
		temp.Listbox1.__init__( self, parent )
		self.a = parent
		self.a.SetBackgroundColour(wx.Colour(4,109,64))

		print (self.a.op_tomb)
		
		
# 		['Abstractor', 'Academic Advisor', 'Account Executive', 'Accountant', 'Accountant, Cost', 'Accountant, Property', 'Accountant, Systems', 'Accountant, Tax', 'Accountant Clerk', 'Acquisitions Librarian', 'Auditor, Internal', 'Auto Design Detailer', 'Automobile Body Repair Supervisor', 'Automobile Body Repairer', 'Automobile Detailer', 'Automobile Mechanic', 'Automobile Racer', 'Automobile Rental Clerk', 'Automobile Service Station Attendant', 'Automobile Service Station Mechanic', 'Automobile Tester, Governmental Services', 'Automobile Engineering Technician', 'B', 'Baggage and Mail Agent', 'Baggage Handler', 'Bailiff', 'Baker', 'Ballistics Expert, Forensic', 'Bank Examiner', 'Bank Teller', 'Bank Teller Supervisor', 'Barber', 'Barista', 'Bartender', 'Bibliographer', 'Bicycle Repairer', 'Billing Clerk', 'Bindery Worker, Printing and Publishing', 'Biochemist', 'Biofuel Processing Technician', 'Bioinformatics Scientist', 'Bioinformatics Technician', 'Biological Aide', 'Biological Scientist', 'Biologist', 'Biomass Plant Technician', 'Biomedical Equipment Technician', 'Biophysicist', 'Biostatistician', 'Blaster', 'Blind Aide', 'Boat Outfitter', 'Boat Repairer', 'Bodyguard', 'Boilermaker', 'Bookbinder', 'Border Guard', 'Botanist', 'Bricklayer', 'Bricklayer Supervisor', 'Bridge Inspector', 'Broadcast Checker', 'Broadcast News Analyst', 'Broadcast Technician', 'Brokerage Clerk', 'Budget Analyst', 'Budget Clerk', 'Budget Officer', 'Building Cleaner', 'Building Inspector', 'Building Insulation Supervisor', 'Building Superintendent', 'Bulldozer Operator', 'Bureau Chief', 'Business Consultant', 'Business Continuity Planner', 'Business Enterprise Officer', 'Business Intelligence Analyst', 'Business Manager, College or University', 'Business Representative, Labor Union', 'Butcher', 'Buyer', 'Buyer, Farm Products', 'C', 'Cabinet Assembler', 'Cabinetmaker', 'Cable Splicer', 'Cake Decorator', 'Calibration Laboratory Technician', 'Camera Operator, Television, Video, and Film', 'Camera Repairer', 'Camp Director', 'Cardiologist', 'Cardiopulmonary Technologist', 'Casdiovascular Technologist and Technician', 'Career Counselor', 'Cargo and Freight Agent', 'Carpenter', 'Carpet Layer', 'Cartoonist', 'Philebotomist ', 'Photo Technician', 'Photogrammetrist', 'Photograph Retoucher', 'Photographer, Still', 'Photographic Process Worker', 'Photojournalist', 'Physitrist', 'Physical Eeductaion Instructor', 'Physical Therapist', 'Physical Therapist Assistant', 'Physical Therapy Aide', 'Physician Assistant', 'Physician, General Practioner', 'Physician, Internist', 'Physician, Naturopathic', 'Physician, Nuclear Medicine', 'Physician, Occupational ', 'Physician, Osteopathic Medicine', 'Physician, Preventive Medicine', 'Physician, Sports Medicine', 'Physicist', 'Physiologist', 'Piano Technician', 'Piano Tuner', 'Picture Framer', 'Pilot, Airplane', 'Pilot, Commercial Airplane', 'Pilot, Executive', 'Pilot, Helicopter', 'Pilot, Highway Patrol', 'Pipe Fitter', 'Pipelayer', 'Pipelines Supervisor', 'Placement Director', 'Planetarium Technician', 'Plant Pathologist', 'Plant Supervisor', 'Plasterer and Stucco Mason', 'Plating and Coating Machine Operator', 'Playwright', 'Plumber', 'Podiatrist', 'Poet', 'Police Captain, Precinct', 'Police Officer', 'Police Officer, Crime Prevention', 'Police Officer, Safety Instruction', 'Police Officer, State Highway', 'Political Scientist', 'Politician', 'Pllution Control Technician', 'Polygrapgh Examiner', 'Post Office Clerk', 'Postal Service Mail Carrier', 'Pstmaster', 'Precision Agriculture Technician', 'Preparation Plant Supervisor', 'Prepress Technician', 'President, Educational Institution', 'President, Financial Institution', 'Press Operator', 'Preventive Maintenance Coordinator', 'Print Binding and Finishing Worker', 'Printed Circuit Desiger', 'Printing Machine Operator', 'Printmaker', 'Private  Investigator', 'Probation/Parole Officer', 'Process Artist, Printing and Publishing ', 'Process Server', 'Procurement Clerk', 'Producer, Film', 'Producer, Radio and TV', 'Production Clerk', 'Production Coordinator', 'Production Laborer', 'Production Manager', 'Production Manager, Advertising', 'Production Planner', 'Production Superintendent, Agriculture', 'Program Administrator, Alcohol and Drug Abuse Assistance', 'Program Coordinator, Amusement and Recreation', 'Program Manager', 'Program Services Planner', 'Project Manager, Environmental Research', 'Projectionist, Chief', 'Proofreader', 'Property Clerk', 'Prospector', 'Prosthetics Technician', 'Prosthetist', 'Prosthodontist', 'Psychiatric Aide', 'Psychiatric Aide Instructor', 'Psychiatric Aide, Mentally Challenged', 'Psychiatric Technician', 'Psychiatrist', 'Psychologist, Chief', 'Psychologist, Clinical', 'Psychologist, Counseling', 'Psychologist, Educational', 'Psychologist, Experimental', 'Psychologist, Industrial-Organizational', 'Psychologist, School', 'Psychometrist', 'Public Health Service Officer', 'Public Relations Representative', 'Public Relations Specialist', 'Pulmonary Function Technician', 'Puppeteer', 'Purchasing Agent', 'Purification Operator', 'Q', 'Quality Assurance Analyst/Tester', 'Quality Control Analyst', 'Quality Control Clerk, Drug Preparation and Relate prodducts', 'Quality Control Coordinator', 'Quality Control Technician, Food Preparation', 'Quality Control Technician, Manufactured Products', 'R', 'Radiation Monitor', 'Radiation Protection Specialist', 'Radiation Therapy Technologist', 'Radio Frequency Identification Device Specialist', 'Radio Operator', 'Radio Cellular, and Tower Equipment Installer and Repairer', 'Radiologic Technician', 'Radiologic Technologist', 'Radiologic Technologist, Chief', 'Radiological Equipment Specialist', 'Radiologist', 'Radiopharmacist', 'Railway Equipment Operator', 'Range Manager', 'Rate Analyst, Freight', 'Real Estate Broker', 'Receipt and Report Clerk', 'Receptionist', 'Recreation Aide', 'Recreation Leader', 'Recreation Supervisor', 'Recreational Therapist', 'Recruiter', 'Recycling and Reclamation Worker', 'Recycling Coordinator', 'Referral Clerk, Temporary Employment Agency', 'Refinery Operator, Grain', 'Refrigeration Mechanic', 'Refuse and Recyclable Material Collector', 'Registrar, College or University', 'Registrar, Museum', 'Regulatory Affairs Specialists', 'Reinforcing Iron and Rebar Worker', 'Remote Sensing Scientist/Technologist', 'Remote Sensing Technician ', 'Repairer, Art Objects', 'Repairer, Electronics and Computers ', 'Repairer, Welding Equipment', 'Reporter/News Correspondent', 'Research Contracts Supervisor', 'Research Director', 'Reservation Clerk', 'Reservations Agent, Air Transportation', 'Residental Advisor', 'Respiratory Therapist', 'Respiratory Therapy Aide', 'Respiratory Therapy Technician', 'Restorer, Ceramic', 'Restorer, Paintings', 'Restorer, Paper and Prints', 'Revenue Agent', 'Rigger', 'Risk Management Specialist', 'Road Supervisor', 'Robot Technician', 'Roofer ', 'Roustabout, Oil and Gas', 'Route Supervisor', 'S', 'Safety Clothing and Equipment Designer', 'Safety Inspector', 'Safety Inspector, Truck', 'Safety Manager, Medical Services', 'Sales Agent, Financial Services', 'Sales Agent, Insurance', 'Sales Agent, Real Estate', 'Sales Agent, Securities and Commodities', 'Sales Clerk', 'Sales Correspondent', 'Sales Representative , Advertising', 'Sales Representative, Farm and Garden Equipment and Supplies', 'Sales Representative, Footwear', 'Sales Representative, Graphic Art', 'Sales Representative, Hobbies and Crafts', 'Sales Representative, Household Appliances', 'Sales Representative, Office Machines', 'Sales Representative, Security Systems', 'Sales Representative, Technical and Scientific Products', 'Salesperson, Apparel and Accessories', 'Salesperson, Automobiles', 'Salesperson, Books', 'Salesperson, Cosmetics and Toiletries', 'Salesperson, Flowers', 'Salesperson, General Merchandise', 'Salesperson, Musical Instruments and Accessories', 'Salesperson, Pianos and Organs', 'Salesperson, Sporting Goods', 'Sampler, Minerals and Eraths', 'Sanitarian', 'Sanitation Inspector', 'Sanitation Superintendent', 'Sanitation Supervisor', 'Satellite Communications Technician', 'Sawing Machine Operator', 'Scenic Arts Supervisor', 'Schedule Maker', 'School Crossing Guard', 'School Principal', 'School/Guidance Counselor', 'Screen Writer', 'Scuba Diver', 'Sculptor', 'Search Marketing Strategist', 'Secretary', 'Securities Clerk', 'Securities Trader, Financial', 'Security and Fire Alarm Systems Installer', 'Security Consultant ', 'Security Guard', 'Security Manager', 'Seismologist', 'Semiconductor Technician', 'Service Manager, Automobile Services', 'Service Unit Operator, Oil, Gas, and Mining', 'Set Decorator, Theater and Film', 'Set Designer, Theater and Film', 'Sewer System Supervisor', 'Sewing Machine Operator', 'Sheet Metal Worker', 'Sheriff/Deputy Sheriff', 'Ship Captain', 'Ship Mate', 'Ship Pilot', 'Shipfitter', 'Shipping and Receiving Clerk', 'Shipping anf Receiving, Order Clerk', 'Shoe Repairer', 'Shopping Investigator', 'Show Operations Supervisor', 'Sign Shop Supervisor', 'Silversmith', 'Siger', 'Singing Messenger', 'Skin Care Specialist', 'Small Engine Mechanic', 'Social Director', 'Social Science Research Assistant', 'Social Services Aide', 'Social Welfare Administrator', 'Social Worker ', 'Sociologist', 'Software Developer', 'Software Quality Assurance Engineer and Tester', 'Soil Conservation Technician', 'Soil Conservationist', 'Solar Energy Systems Designer', 'Solar Fabrication Technician', 'Solar Photovoltaic Installer', 'Solar Sales Representative and Assessor', 'Solar Thermal Installer/Technician', 'Solderer and Brazer', 'Sound Effects Technician', 'Sound Mixer ', 'Sound Technician', 'Special Agent, Customs', 'Special Agent, Governmental Services', 'Special Education Supervisor', 'Speech-Language Pathologist', 'Speech-Language Pathology Assistant', 'Stage Manager', 'Stage Technician', 'Statement Clerk', 'Station Manager, Radio and TV', 'Station Manager, Railroad', 'Statistical Assistant', 'Statistician', 'Stock Clerk', 'Stock Control Clerk', 'Stock Transfer Clerk', 'Stockbroker', 'Stone Carver', 'Stonemason', 'Stress Analyst', 'Structural Metal Fabricator and Fitter', 'Substance Abuse Counselor', 'Substation Operator, Utilities', 'Superintendent of Schools', 'Surgeon', 'Surgical Assistant', 'Surveillance System Monitor', 'Survey Researcher', 'Survey Worker Supervisor', 'Surveyor, Geodetic', 'Surveyor, Hydrographic', 'Surveyor, Land', 'Surveyor, Ship', 'Sustainability Specialist', 'Switchboard Operator/Answering Service Operator', 'systems Analyst', 'T', 'Tailor', 'Talent Manager', 'Taper/Finisher', 'Tax Preparer', 'Taxicab Coordinator', 'Teacher Aide', 'Teacher, Adult Education', 'Teacher, Art', 'Teacher, Drama', 'Teacher, Elementary School', 'Teacher, Elementary School, Special Education', 'Teacher, Industrial Arts', 'Teacher, Kindergarten', 'Teacher, Middle School, Special Education', 'Teacher, Music', 'Teacher, Preschool', 'Teacher, Preschool, Special Education', 'Teacher, Secondary School', 'Teacher, Secondaru School, Special Education', 'Techical Support Specialist', 'Technical Writer', 'Technician, Dialysis', 'Technician, Surgical', 'Telecommunications Engineering Specialist', 'Telecommunications Equipment Installer and Repairer', 'Telecommunications Line Installer and Repairer', 'Telecommunications Specialist', 'Telecommunications Technician', 'Telecommunicator Supervisor', 'Telemarketer', 'Television Production Clerk', 'Television Technician', 'Terrazo Worker and Finisher', 'Test Technician', 'Ticket Sales Agent', 'Ticket Sales Supervisor', 'Tire Repairer and Changer', 'Tissue Technologist', 'Title Examiner', 'Tool and Die Maker', 'Tools Designer', 'Tools Programmer, Numerical Control', 'Town Clerk', 'Toxicologist', 'Toxicologist, Chief', 'Tractor Operator', 'Traffic Checker', 'Traffer Clerk', 'Traffic Maintenance Supervisor', 'Traffic Manager', 'Traffic Technician', 'Train Dispatcher', 'Training and Development Specialist', 'Transportation Director', 'Transportation Inspector', 'Transportation Manager', 'Transportation Planner', 'Transportation Security Officer', 'Travel Agent', 'Tree Surgeon', 'Tree Trimmer/Pruner', 'Tutor', 'Typist/Transcriptionist', 'U', 'Ultrasound Technologist', 'Umpire/Referee', 'Underwriter', 'Upholsterer', 'Upholsterer, Chair and Furiture', 'Urban Planner', 'Urologist', 'Usher, Lobby Attendant, and Ticket Taker', 'Utilities Service Investigator', 'Utility Clerk', 'V', 'Vendor Quality Supervisor', 'Veteranian', 'Veterinary Assistant', 'Veterinary Livestock Inspector', 'Veterinary Technologist and Technician', 'Video Game Designer', 'Video Game Programmer', 'Vision Rehabilitation Therapist', 'Vocational Rehabilitation Consultant', 'Vocational Rehabilitation Counselor', 'Voice Pathologist', 'Volunteer Services Supervisor', 'W', 'Waiter/Waitress', 'Waiter/Waitress, Head', 'Warehouse Supervisor', 'Watch Repairer', 'Water Quality Tester', 'Water Resources Specialist', 'Water Treatment Plant Operator', 'Water Treatment Plant Supervisor', 'Water/Sewer Systems Superintendent', 'Weather Observer ', 'Weatherization Installer/Technician', 'Weaver, Carpet and Rug', 'Web Administrator', 'Web Developer/Designer', 'Wedding Consultant', 'Welder', 'Welding Machine Operator', 'Welfare Director', 'Wholesaler', 'Wildlife Control Agent', 'Wind Energy Project Manager', 'Wind Turbine Service Technician', 'Wine Maker', 'Woodworking Machine Operator', 'Winter, Fiction and Nonfiction', 'Y', 'Yard Manager, Railroad Transportation', 'Z', 'Zoo Veterinarian', 'Zoologist']

	# Handlers for Listbox events.
	def m_tombolcancel_lb(self, event):
		
		print ("tombol cancel")
		self.Close()
		# TODO: Implement m_tombolcancel_lb
		pass

	def tombolok_lb( self, event ):
		self.Value = self.m_listBox1.GetString(self.m_listBox1.GetSelection())

		if self.a.op_tomb == 1:

			self.a.m_panelPage2.textctrl1.SetValue(self.Value)
			print ("kesini")
		elif self.a.op_tomb == 2:

			self.a.m_panelPage2.textctrl2.SetValue(self.Value)
			print ("kesini")			
		elif self.a.op_tomb == 3:

			self.a.m_panelPage2.textctrl3.SetValue(self.Value)
			print ("kesini")			

		elif self.a.op_tomb == 4:

			self.a.m_panelPage2.textctrl4.SetValue(self.Value)
			print ("kesini")			
		elif self.a.op_tomb == 5:

			self.a.m_panelPage2.textctrl5.SetValue(self.Value)
			print ("kesini")			
		elif self.a.op_tomb == 6:

			self.a.m_panelPage2.textctrl6.SetValue(self.Value)
			print ("kesini")			

		else :
			print("salah")
			
		
		
		self.Close()
		print ("tombol ok")
		# TODO: Implement tombolok_lb
		pass

	def m_listboxselect( self, event ):
		self.Close()
		# TODO: Implement m_listboxselect
		pass


