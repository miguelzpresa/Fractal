#!/usr/bin/env python3
def give_me_lenght(b=[[-1,0],[1,0]]): #euclidian distance
  x1,x2,y1,y2=b[0][0],b[1][0],b[0][1],b[1][1] 
  print(x1,x2,y1,y2)
  return np.sqrt((x2-x1)**2+(y2-y1)**2)
print(give_me_lenght())




def inner_points(partialongl,who:int,val=[]): # who es de quien,a quien se modifica si a x o a y
  #0, [-1, 0]
  val[who]=val[who] +partialongl
  
  print(f"point1{val}")

  point1 = np.round(val,1) 
  point2=point1.copy()
  point2[who] = point1[who]+ partialongl  
  print(f"point2{point2}")
  #BasisBuffer(point1,point2)
  return (point1,point2) #return la tupla actualizada



def startp(b= [[-1,0],[1,0]]): # != a los valores de los indices de a continuación
  
  totallongline = give_me_lenght(b)
  partiallongline = totallongline *.3
  print((f"partiallong{partiallongline}"))
  if b[0][0] == b[1][0]:  # base es vertical(xs  fijas)
  
    if b[0][1] > b[1][1]: startpoint =(1,[b[1][0], b[1][1]],[b[0][0],b[0][1]]) # start point is #el 1 indica cual de los elementos de la tupla(si x=0 o si y=1,seran la literal a sumarle el sumando )
    else:startpoint = (1,[b[0][0],b[0][1]],   [b[1][0],b[1][1]])
  else:  #base es horizontal(ys fijas) osea que b[0,1]==b[1,1]

    if b[0][0] > b[1][0]:startpoint =(0,[b[1][0], b[1][1]], [b[0][1],b[0][1]])
    else:startpoint =(0,[b[0][0],b[0][1]], [b[1][0],b[1][1]])
  
  print(f"el el startpoint es{startpoint}")
  return (partiallongline,startpoint[0],startpoint[1],startpoint[2]) # startpoint[0] es who(quien varía 0 si x y 1 si y),startpoint[1] es el punto startpoint 
  #startpoint2 es el endpoint
  
  
  def parallel_p(longi,segmento,tipo): #yields the new points from basis points
  #long = give_me_lenght(segmento)
  longi=tipo
  p1,p2 = segmento
  p3=p1.copy()
  p4=p2.copy()
  mutator =0
  signo = True #positivo
  if tipo == 0: # bder
    signo= True
    mutator =0
  elif tipo == 1: #bsup
    signo= True
    mutator =1
  elif tipo == 2: #bizq
    signo= False
    mutator =0
  elif tipo == 3: #binf
    signo= False
    mutator =1

  if signo :
    p3[mutator]+=longi
    p4[mutator]+=longi
  else:
    p3[mutator]-=longi
    p4[mutator]-=longi
  #print(type(p1))
  #print(type(p3))
  #print([p1,p2],[p1,p3],[p2,p4],[p3,p4])
  return ([[tipo], [p1,p2],  [p1,p3],  [p2,p4],   [p3,p4] ])


def plot_basis(sp,ep,innerpoints:tuple):
  p1,p2 = innerpoints
  ys=[]
  xs=[]
  xs = [[sp[0],p1[0],[ep[0],p2[0]]]
  ys = [[sp[1],p1[1],[ep[1],p2[1]]]
  ax.plot(xs,ys,color='green', marker='o')

def final_plot(BasissBuffer):
  for i,rows in enumerate(BasissBuffer):
    xs =[]
    ys = []
    xs.append(BasissBuffer[i][0])
    ys.append(BasissBuffer[i][1])
    ax.plot(xs,ys,color='blue',marker ="*")
  
parallel_p(0.6, (([-0.4,  0. ]),([0.2, 0. ])),1)

#------------------------------------------------------------------------

if__name__=="__main__":

  basis_buffer=[[8,0],[-8,0]]
  l= 16
  f,ax = plt.subplots()



  fractal_iter = int(input())
  if fractal_iter == 0:
    ax.plot()
  for it in range(fractal_iter):
    for i,b in enumerate(basis_buffer):
      aux_b_buffer =[]

      while it < (fractal_iter-2):
        l,who,sp,ep,o = startp(b)
        tipo =i% 4
        TODO = parallel_p(l,sp,ep,tipo)
        for line in TODO:
          ll,whoo,spp,epp = startp(line)
          tipoo =i% 4
          inpoo = inner_points(ll,whoo,spp)
          plot_basis(spp,epp,inpoo)
          aux_b_buffer.append(parallel_p(ll,inpoo,typoo))
      if fractal_iter != 1:
        for line in aux_b_buffer:
          final_plot()
      else:
        closing = parallel_p(l,b,4)
        final_plot(basis_buffer)


  basis_buffer =[]
  basis_buffer = aux_b_buffer.copy()
  aux_b_buffer = []
  
