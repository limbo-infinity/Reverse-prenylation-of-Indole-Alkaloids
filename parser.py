import re
import csv

def part_orb_energies(file, name):
    energies = []
    energies_tup = []
    read = False
    
    with open(file, "r") as f:
        for line in f:
            
            if "ORBITAL ENERGIES" in line.upper():
                print(line)
                read = True
                next(f)
                next(f)
                continue
            if read and line.strip() == "":
                break
            
            if read:
                print(repr(line))
                match = re.findall(r'[+-]?\d*\.\d+|\d+', line)
                if len(match) >= 3:     
                    print(match)
                    energies.append(f'Orbital: {float(match[0])} Occupancy: {match[1]} Energy(ev): {match[3]}')
                    energies_tup.append((float(match[0]), float(match[1]), float(match[2]), float(match[3])))
                
    with open(f'energies_{name}.csv', 'w', newline="") as out:
        writer = csv.writer(out)
        
        writer.writerow(["NO", "OCC", "E(Eh)", "E(eV)"])
        
        for row in energies_tup:
            writer.writerow(row)
        
    
    
    return [energies, energies_tup]




print(part_orb_energies('Tests/water.out', 'water')[1])
print(part_orb_energies('Indole/Propargyl_indole/indole.out', 'C3 propargyl indole')[1])
