import random
import math 
import runpy

data = open("data_latih.csv","r")

def generate():
	number=[]
	x=1
	for x in range (10):
		p = list(range(0,9))
		result = random.sample(p, k=6)
		number.append(result)
	return number

def decode(n):
	x1 = -3+(((3+3)/(9*(pow(10,-1)+pow(10,-2))))*(n[0]*pow(10,-1)+n[1]*pow(10,-2)))
	x2 = -2+(((2+2)/(9*(pow(10,-1)+pow(10,-2))))*(n[2]*pow(10,-1)+n[3]*pow(10,-2)))
	return x1,x2

def decode_chromosome(number):
	chromosome_rslt=[]
	for n in number:
		x1 = -3+(((3+3)/(9*(pow(10,-1)+pow(10,-2))))*(n[0]*pow(10,-1)+n[1]*pow(10,-2)))
		x2 = -2+(((2+2)/(9*(pow(10,-1)+pow(10,-2))))*(n[2]*pow(10,-1)+n[3]*pow(10,-2)))
	chromosome_rslt.append([x1,x2])
	return chromosome_rslt

def count_fitness(chromosome_rslt):
	fit=[]
	fitness=[]
	for m in chromosome_rslt:
		a = (((4-2.1*1*(pow(m[0],2)))+(pow(m[0],4))/3)*pow(m[0],2))+m[0]*m[1]+(((-4)+4*pow(m[1],2)))*pow(m[1],2)
		fit.append(a)
	
	for y in fit:
		b=1/(y+10)
		fitness.append(b)
	return fitness

def best_fitness(fitness):
	max=0
	idx=0
	for i in range(len(fitness)):
		if fitness[i] > max:
			max=fitness[i]
			print(fitness[i])
			idx=i
	print(max)
	return max,idx

def best_chromosome(max, fitness_list, pop):
	idx=-1
	for i in range(len(fitness_list)):
		if max == fitness_list[i]:
			idx=i
	return pop[idx]

def best_value(chrom):
	x1 = -3+((3+3)/(9*(pow(10,-1)+pow(10,-2))))*(chrom[0]*pow(10,-1)+chrom[1]*pow(10,-2))
	x2 = -2+((2+2)/(9*(pow(10,-1)+pow(10,-2))))*(chrom[2]*pow(10,-1)+chrom[3]*pow(10,-2))
	a = (((4-2*1*(pow(x1,2)))+(pow(x1,4))/3)*pow(x1,2))+x1*x2+(((-4)+4*pow(x2,2)))*pow(x2,2)
	return a,x1,x2

def value(x1,x2):
	return (((4-2*1*(pow(x1,2)))+(pow(x1,4))/3)*pow(x1,2))+x1*x2+(((-4)+4*pow(x2,2)))*pow(x2,2)

def parent(fitness):
	total = 0
	for x in fitness:
		total += x
	i = []
	for m in range(2):
		r = random.random()
		individu = 0 
		while (r>0) and (individu<=8):
			r -= fitness[individu]/total
			individu=individu+1
		i.append(individu)
	return i

def search(number,index):
	n1 = index[0]
	n2 = index[1]
	c1 = number[n1]
	c2 = number[n2]
	return c1,c2

def crossover(n1,n2):
	womb = random.randint(0,2)
	bomb = random.random()
	if bomb<0.1:
		if womb == 2:
			n1[2],n2[2]=n2[2],n1[2]
			return n1,n2
		elif womb == 1:
			n1[2],n2[2],n1[1],n2[1]=n2[2],n1[2],n2[1],n2[1]
			return n1,n2
		elif womb ==0:
			n1[2],n2[2],n1[1],n2[1],n1[0],n2[0]=n2[2],n1[2],n2[1],n1[1],n2[0],n1[0]
			return n1,n2
	else :
		return n1,n2

def mutation(n1,n2):
	mutation_rslt =[]
	for i in range(len(n1)):
		chance1 = random.random()
		if chance1<0.1:
			n1[i]=random.randint(0,9)

	for j in range(len(n2)):
		chance2 = random.random()
		if chance2<0.1:
			n2[j]=random.randint(0,9)

	mutation_rslt.append(n1)
	mutation_rslt.append(n2)
	return mutation_rslt

pop = generate()
decode = decode_chromosome(pop)
fitness = count_fitness(decode)

print("populasi awal :",pop)


#def general_replacement(pop_global):
#	new_pop = []
#	new_pop = pop_global
#	arrStorage.append(new_pop[0])
#	arrStorage.append(new_pop[1])
#	return new_pop

gen=0
best_global = best_fitness(fitness)
while gen<=1000:
	arrStorage = []
	for x in range(5):
		decode = decode_chromosome(pop)
		fitness = count_fitness(decode)
		idx = parent(fitness)
		n1,n2 = search(pop,idx)
		child1,child2 = crossover(n1,n2)
		mutation_rslt = mutation(child1,child2)
		arrStorage.append(mutation_rslt[0])
		arrStorage.append(mutation_rslt[1])

	pop = arrStorage
	decode = decode_chromosome(pop)
	fitness = count_fitness(decode)
	best_local = best_fitness(fitness) 
	#best_pop = general_replacement(best_local)

	print(best_local[0])
	if best_local[0]>best_global[0]:
		best_global = best_local
		pop_global = best_chromosome(best_global, fitness, pop)
		best_val,x1,x2 = best_value(pop_global)
	#	new_pop = best_pop(new_pop)

	gen+=1

print("fitness terbaik : ", best_global)
print("kromosom terbaik : ", pop_global)
print("minimum value : ", best_val)
print("encoded : ",x1," ",x2)
#print("new population :", best_pop)
# READ ME : hapus comment ketika sudah sekali run program for surprise
#kecuali line 169 & 170. terima kasih :)
