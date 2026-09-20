from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
import numpy as np

OUT = Path(__file__).resolve().parents[1] / 'assets' / 'figures'
OUT.mkdir(parents=True, exist_ok=True)
BLUE='#2454dc'; INK='#17233c'; MUTED='#5c6780'; GRAY='#8794ad'; LINE='#e1e6ef'
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':12,'text.color':INK,'axes.labelcolor':MUTED,'xtick.color':MUTED,'ytick.color':INK,'svg.fonttype':'none','figure.facecolor':'white','savefig.facecolor':'white'})
def save(fig,name):
 fig.savefig(OUT/(name+'.svg'),bbox_inches='tight',pad_inches=.25)
 fig.savefig(OUT/(name+'.png'),dpi=160,bbox_inches='tight',pad_inches=.25)
 plt.close(fig)

# Separate scales for financial model outputs and participant counts.
fig,axs=plt.subplots(3,1,figsize=(8.8,8.4));fig.subplots_adjust(hspace=.92,left=.21,right=.85,top=.85,bottom=.08)
fig.text(.03,.96,'Master vs. separate protocols',fontsize=20,weight='bold')
fig.text(.03,.913,'Best candidates in the reported search grid · modeled use case',fontsize=12,color=MUTED)
for ax,title,vals,limit,unit in zip(axs,['Risk-adjusted net value','Expected development cost','Enrollment'],[[427.8,369.8],[90.4,143.1],[603,621]],[500,175,700],['USD millions','USD millions','Participants']):
 ax.barh([1,0],vals,color=[BLUE,GRAY],height=.48)
 ax.set_yticks([1,0],['Master','Separate']);ax.set_xlim(0,limit);ax.set_ylim(-.55,1.55)
 ax.set_title(title,loc='left',fontsize=14,weight='bold',pad=15)
 ax.set_xlabel(unit,fontsize=11);ax.tick_params(axis='both',length=0,labelsize=11)
 ax.xaxis.grid(True,color=LINE);ax.set_axisbelow(True)
 for sp in ax.spines.values():sp.set_visible(False)
 for y,val in zip([1,0],vals):ax.text(val+limit*.018,y,f'${val:,.1f}M' if unit=='USD millions' else f'{val:,}',va='center',fontsize=12,weight='bold')
fig.text(.03,.015,'Protocol-strategy project with Naishu Kui (2026). Modeled financial outcomes.',fontsize=10,color=MUTED)
save(fig,'protocol-model-comparison')

def box(ax,x,y,w,h,label,fill='#edf2ff',color=INK,fontsize=12):
 ax.add_patch(FancyBboxPatch((x,y),w,h,boxstyle='round,pad=0.013,rounding_size=0.015',linewidth=1,edgecolor=LINE,facecolor=fill))
 ax.text(x+w/2,y+h/2,label,ha='center',va='center',fontsize=fontsize,color=color,linespacing=1.5)
def arrow(ax,x1,y1,x2,y2):
 ax.add_patch(FancyArrowPatch((x1,y1),(x2,y2),arrowstyle='-|>',mutation_scale=13,color=GRAY,linewidth=1.5))
fig,ax=plt.subplots(figsize=(10,6.5));ax.set_xlim(0,1);ax.set_ylim(0,1);ax.axis('off')
ax.text(0,.97,'Two paths when monotherapy is ready first',fontsize=18,weight='bold')
ax.text(0,.915,'Conceptual comparison · timing and allocation are not to scale',fontsize=11,color=MUTED)
ax.text(.0,.8,'MASTER PROTOCOL',fontsize=11,weight='bold',color=BLUE)
box(ax,.02,.57,.34,.14,'Monotherapy vs. control')
box(ax,.6,.57,.36,.14,'Monotherapy + combination\ncomparisons with shared control')
arrow(ax,.38,.64,.575,.64);ax.text(.48,.72,'Amendment /\nadd combination',ha='center',fontsize=10,color=MUTED)
ax.text(.02,.49,'Sharing requires an appropriate control comparison and a prespecified evidence plan.',fontsize=10,color=MUTED)
ax.axhline(.43,color=LINE,lw=1)
ax.text(.0,.36,'SEPARATE PROTOCOLS',fontsize=11,weight='bold',color=MUTED)
box(ax,.02,.12,.39,.15,'Trial A\nMonotherapy vs. its control',fill='#f6f8fc')
box(ax,.56,.12,.4,.15,'Trial B\nCombination vs. its control',fill='#f6f8fc')
ax.text(.02,.045,'Start monotherapy when ready',fontsize=11,color=MUTED)
ax.text(.56,.045,'Start combination when ready',fontsize=11,color=MUTED)
save(fig,'protocol-pathways')

fig,ax=plt.subplots(figsize=(9,7));ax.set_xlim(0,1);ax.set_ylim(0,1);ax.axis('off')
ax.text(0,.98,'Routine tissue to a development decision',fontsize=19,weight='bold')
ax.text(0,.928,'Proposed application informed by computational-pathology research',fontsize=11,color=MUTED)
steps=[(.73,'1  Define the information gap','Prognostic risk, a biomarker hypothesis or assay prioritization'),(.52,'2  Test the image-derived signal','Patient-level separation · independent cohorts · uncertainty'),(.31,'3  Establish the intended use','Prognostic risk does not establish differential treatment benefit'),(.10,'4  Decide whether to expand','Value of added information vs. validation and implementation cost')]
for y,title,desc in steps:
 box(ax,.035,y,.93,.14,'',fill='#f6f8fc')
 ax.text(.065,y+.097,title,fontsize=13,weight='bold')
 ax.text(.065,y+.041,desc,fontsize=11,color=MUTED)
 if y>.1:arrow(ax,.5,y-.012,.5,y-.055)
save(fig,'pathology-decision-pathway')

fig,ax=plt.subplots(figsize=(9.5,6.0));fig.subplots_adjust(left=.17,right=.95,top=.72,bottom=.2)
fig.text(.025,.945,'Dose selection under increasing toxicity',fontsize=19,weight='bold')
fig.text(.025,.885,'How often was the safer, efficacious lower dose favored?',fontsize=12,color=MUTED)
values=[81.7,96.5,99.6]; comparator=[45.4,72.7,86.5]
y=np.array([2,1,0]);height=.29
ax.barh(y+.17,values,height=height,color=BLUE,label='Two-stage framework')
ax.barh(y-.17,comparator,height=height,color=GRAY,label='Aggregate-score comparator')
ax.set_yticks(y,['Scenario 1','Scenario 2','Scenario 3']);ax.set_xlim(0,100)
ax.set_xticks([0,25,50,75,100],['0%','25%','50%','75%','100%']);ax.set_axisbelow(True);ax.xaxis.grid(True,color=LINE)
ax.tick_params(length=0);ax.set_xlabel('Lower dose favored (%)',fontsize=11,labelpad=10)
for offset,vals in [(.17,values),(-.17,comparator)]:
 for yy,v in zip(y,vals):ax.text(v-1.5,yy+offset,f'{v}%',ha='right',va='center',color='white' if offset>0 else INK,fontsize=11,weight='bold')
for sp in ax.spines.values():sp.set_visible(False)
ax.legend(loc='lower left',bbox_to_anchor=(-.01,1.02),frameon=False,ncol=2,fontsize=10.5,handlelength=1.4,columnspacing=2)
fig.text(.025,.065,'50 patients per arm · 1,000 simulated trials per scenario · Scenario-specific results',fontsize=10,color=MUTED)
fig.text(.025,.025,'Chakraborty, Dubey, Kumar & Chan (2026)',fontsize=10,color=MUTED)
save(fig,'dose-selection-simulations')
print('Created 4 figures in SVG and PNG.')
