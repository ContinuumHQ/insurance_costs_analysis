import csv

ages = []
sexes = []
bmis = []
children = []
smoker_statuses = []
regions = []
insurance_charges = []

data_file = 'data/insurance.csv'

with open(data_file, newline='') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    
    for row in csv_reader:
        ages.append(int(row['age']))
        sexes.append(row['sex'])
        bmis.append(float(row['bmi']))
        children.append(int(row['children']))
        smoker_statuses.append(row['smoker'])
        regions.append(row['region'])
        insurance_charges.append(float(row['charges']))


class InsuranceAnalysis:
    
    def __init__(self, ages, sexes, bmis, children, smoker_statuses, regions, insurance_charges):
        self.ages = ages
        self.sexes = sexes
        self.bmis = bmis
        self.children = children
        self.smoker_statuses = smoker_statuses
        self.regions = regions
        self.insurance_charges = insurance_charges

    def calculate_smoker_cost_difference(self):
        smoker_costs = []
        non_smoker_costs = []
        
        for i in range(len(self.smoker_statuses)):
            if self.smoker_statuses[i] == 'yes':
                smoker_costs.append(self.insurance_charges[i])
            else:
                non_smoker_costs.append(self.insurance_charges[i])

        avg_smoker = sum(smoker_costs) / len(smoker_costs) if smoker_costs else 0
        avg_non_smoker = sum(non_smoker_costs) / len(non_smoker_costs) if non_smoker_costs else 0
        
        difference = avg_smoker - avg_non_smoker
        
        print('\nAnalyse 1: Kostenunterschied Raucher vs. Nichtraucher')
        print(f'  Anzahl Raucher: {len(smoker_costs)}, Nichtraucher: {len(non_smoker_costs)}')
        print(f'  Durchschnittliche Kosten Raucher: ${avg_smoker:,.2f}')
        print(f'  Durchschnittliche Kosten Nichtraucher: ${avg_non_smoker:,.2f}')
        print(f'  Kosten-Differenz: ${difference:,.2f}')
        
        return avg_smoker, avg_non_smoker

    def calculate_region_costs(self):
        
        region_data = {
            'northeast': {'costs': 0, 'count': 0},
            'northwest': {'costs': 0, 'count': 0},
            'southeast': {'costs': 0, 'count': 0},
            'southwest': {'costs': 0, 'count': 0},
        }

        for i in range(len(self.regions)):
            region = self.regions[i]
            charge = self.insurance_charges[i]
            
            if region in region_data:
                region_data[region]['costs'] += charge
                region_data[region]['count'] += 1

        print('\nAnalyse 2: Durchschnittliche Kosten pro Region')
        
        avg_costs = {}
        for region, data in region_data.items():
            if data['count'] > 0:
                avg = data['costs'] / data['count']
                avg_costs[region] = avg
                print(f'  {region.capitalize()}: ${avg:,.2f}')
            
        return avg_costs

    def analyze_age_bmi_and_children(self):
        
        child_costs = {}
        child_counts = {}
        
        for i in range(len(self.children)):
            num_children = self.children[i]
            cost = self.insurance_charges[i]
            
            if num_children not in child_costs:
                child_costs[num_children] = 0
                child_counts[num_children] = 0
            
            child_costs[num_children] += cost
            child_counts[num_children] += 1
            
        print('\nAnalyse 3: Kosten nach Anzahl der Kinder')
        
        sorted_children = sorted(child_costs.keys())
        for num_children in sorted_children:
            avg = child_costs[num_children] / child_counts[num_children]
            print(f'  {num_children} Kinder (N={child_counts[num_children]}): ${avg:,.2f}')


        max_bmi_index = self.bmis.index(max(self.bmis))
        max_cost_index = self.insurance_charges.index(max(self.insurance_charges))
        
        print('\nAnalyse 3 (Zusatz): Extremwerte')
        print(f'Patient mit höchstem BMI ({self.bmis[max_bmi_index]}): Kosten ${self.insurance_charges[max_bmi_index]:,.2f}, Alter {self.ages[max_bmi_index]}')
        print(f'Patient mit höchsten Kosten (${self.insurance_charges[max_cost_index]:,.2f}): BMI {self.bmis[max_cost_index]}, Alter {self.ages[max_cost_index]}')
            
        return child_costs

    def summarize_results(self):
        
        avg_smoker, avg_non_smoker = self.calculate_smoker_cost_difference()
        avg_costs_region = self.calculate_region_costs()
        child_costs_data = self.analyze_age_bmi_and_children()

        print('_'*50)
        print('\nProject Summary: Key Findings')
        print('_'*50)

        print('\n1. DOMINIERENDER KOSTENFAKTOR (Rauchen):')
        print(f'Raucher verursachen durchschnittlich ${avg_smoker - avg_non_smoker:,.2f} mehr Kosten als Nichtraucher.')
        
        print('\n2. REGIONALE UNTERSCHIEDE:')
        print(f"Die höchsten Kosten liegen in der Southeast-Region (ca. ${avg_costs_region.get('southeast'):,.2f}), die niedrigsten in Southwest.")
        
        print('\n3. EINFLUSS DER KINDERANZAHL:')
        print(f'Die durchschnittlichen Kosten variieren von ${child_costs_data.get(0):,.2f} (0 Kinder) bis zu ${child_costs_data.get(5):,.2f} (5 Kinder).')
        
        print('\nFazit: Der stärkste Prädiktor für hohe Kosten ist der Raucherstatus.')


if __name__ == '__main__':
    
    print(f'Anzahl der Datensätze: {len(ages)}')
    print(f'Erste 5 Altersangaben: {ages[:5]}')
    print(f'Erste 5 Kosten: {insurance_charges[:5]}')
    
    analysis_tool = InsuranceAnalysis(ages, sexes, bmis, children, smoker_statuses, regions, insurance_charges)
    
    analysis_tool.summarize_results()