headers="""President's Secretariat
Vice President's Secretariat
Prime Minister's Office
Cabinet
Cabinet Committee Decisions
Cabinet Committee on Economic Affairs (CCEA)
Cabinet Secretariat
Cabinet Committee on Infrastructure
Cabinet Committee on Price
Cabinet Committee on Investment
AYUSH
Other Cabinet Committees
Department of Space
Department of Ocean Development
Department of Atomic Energy
Election Commission
Finance Commission
Ministry of Agriculture & Farmers Welfare
Ministry of Agro & Rural Industries
Ministry of Chemicals and Fertilizers
Ministry of Civil Aviation
Ministry of Coal
Ministry of Commerce & Industry
Ministry of Communications
Ministry of Company Affairs
Ministry of Consumer Affairs, Food & Public Distribution
Ministry of Cooperation
Ministry of Corporate Affairs
Ministry of Culture
Ministry of Defence
Ministry of Development of North-East Region
Ministry of Disinvestment
Ministry of Drinking Water & Sanitation
Ministry of Earth Sciences
Ministry of Education
Ministry of Electronics & IT
Ministry of Environment, Forest and Climate Change
Ministry of External Affairs
Ministry of Finance
Ministry of Fisheries, Animal Husbandry & Dairying
Ministry of Food Processing Industries
Ministry of Health and Family Welfare
Ministry of Heavy Industries
Ministry of Home Affairs
Ministry of Housing & Urban Affairs
Ministry of Information & Broadcasting
Ministry of Jal Shakti
Ministry of Labour & Employment
Ministry of Law and Justice
Ministry of Micro, Small & Medium Enterprises
Ministry of Mines
Ministry of Minority Affairs
Ministry of New and Renewable Energy
Ministry of Overseas Indian Affairs
Ministry of Panchayati Raj
Ministry of Parliamentary Affairs
Ministry of Personnel, Public Grievances & Pensions
Ministry of Petroleum & Natural Gas
Ministry of Planning
Ministry of Power
Ministry of Railways
Ministry of Road Transport & Highways
Ministry of Rural Development
Ministry of Science & Technology
Ministry of Ports, Shipping and Waterways
Ministry of Skill Development and Entrepreneurship
Ministry of Social Justice & Empowerment
Ministry of Statistics & Programme Implementation
Ministry of Steel
Ministry of Surface Transport
Ministry of Textiles
Ministry of Tourism
Ministry of Tribal Affairs
Ministry of Urban Development
Ministry of Water Resources, River Development and Ganga Rejuvenation
Ministry of Women and Child Development
Ministry of Youth Affairs and Sports
NITI Aayog
PM Speech
EAC-PM
UPSC
Special Service and Features
PIB Headquarters
Office of Principal Scientific Advisor to GoI
National Financial Reporting Authority
Competition Commission of India
IFSC Authority
National Security Council Secretariat"""

import os

headers = [i for i in headers.split('\n')]

for header in headers:
    if os.path.exists(f'./assets/headers/{header}.png'):
        print(f'"{header}" : "./assets/headers/{header}.png",')