

lambda_ds_units = ['1', '2', '3', '4', 'cs', 'labs']

core_unit = [c for c in lambda_ds_units if c[0] in ['1', '2', '3', '4']]

print(core_unit)

core_unit = []
for c in lambda_ds_units:
    if c[0] in ['1', '2', '3', '4']:
        core_unit.append(c)
print(core_unit)
