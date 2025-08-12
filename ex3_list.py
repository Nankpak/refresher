noise_makers =[]
noise_makers.append('Dorcas')
noise_makers.append('Bethel')
print(noise_makers, len(noise_makers))
colors = ['blue','black','red','white','yellow','black','green']
print(colors, len(colors))
colors.insert(10,"violet")
print(colors)
fruits = ['orange','mango','apple','pear']
fruits[1] = "grape"
print(fruits)
fruits[0],fruits[-1] = fruits[-1], fruits[0]
fruits = fruits[0:3]
print(fruits)
a = [1,2,3,[4,5,[6,7,[8],9]]]
print(a[3][2][2][0])
print(a[3][2][3])
print(a[3])
