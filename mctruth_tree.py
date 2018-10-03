#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os, sys
sys.path.append("common/")

from gallery_tools import *


# In[2]:


outfile = ROOT.TFile("/uboone/data/users/wketchum/genie_uboone_1M_simple.root", "RECREATE")


# In[3]:


run = array('I',[ 0 ])
event = array('I',[ 0 ])

truth_index = array('I',[ 0 ])
n_particles = array('i',[-1])
origin = array('i',[-1])

mode = array('i',[-1])
interaction_type = array('i',[-1])
ccnc = array('i',[-1])
target = array('i',[-1])
hit_nucl = array('i',[-1])
hit_quark = array('i',[-1])
hadronic_mass = array('d',[-99999])
interaction_x = array('d',[-99999])
interaction_y = array('d',[-99999])
interaction_q2 = array('d',[-99999])
interaction_pt = array('d',[-99999])
interaction_theta = array('d',[-99999])

p_index = array('I',[ 0 ])
status = array('i',[-1])
trackid = array('i',[-1])
pdgcode = array('i',[-1])
mother = array('i',[-1])
process = ROOT.string()
endprocess = ROOT.string()
#daughters = ROOT.vector('int')()
weight = array('d',[-999])
rescatter = array('i',[-1])

start_x = array('d',[-99999])
start_y = array('d',[-99999])
start_z = array('d',[-99999])
start_t = array('d',[-99999])

end_x = array('d',[-99999])
end_y = array('d',[-99999])
end_z = array('d',[-99999])
end_t = array('d',[-99999])

px = array('d',[-99999])
py = array('d',[-99999])
pz = array('d',[-99999])
p = array('d',[-99999])
pt = array('d',[-99999])
e = array('d',[-99999])
mass = array('d',[-999])

end_px = array('d',[-99999])
end_py = array('d',[-99999])
end_pz = array('d',[-99999])
end_e = array('d',[-99999])


mctruth_tree = ROOT.TTree("mctruth_tree","MCTruth Tree")
mctruth_tree.Branch("run",run,"run/i")
mctruth_tree.Branch("event",event,"event/i")
mctruth_tree.Branch('truth_index',truth_index,"truth_index/i")
mctruth_tree.Branch('n_particles',n_particles,"n_particles/I")
mctruth_tree.Branch('origin',origin,"origin/I")
mctruth_tree.Branch('mode',mode,"mode/I")
mctruth_tree.Branch('interaction_type',interaction_type,"interaction_type/I")
mctruth_tree.Branch('ccnc',ccnc,"ccnc/I")
mctruth_tree.Branch('target',target,"target/I")
mctruth_tree.Branch('hit_nucl',hit_nucl,"hit_nucl/I")
mctruth_tree.Branch('hit_quark',hit_quark,"hit_quark/I")
mctruth_tree.Branch('hadronic_mass',hadronic_mass,"hadronic_mass/D")
mctruth_tree.Branch('interaction_x',interaction_x,"interaction_x/D")
mctruth_tree.Branch('interaction_y',interaction_y,"interaction_y/D")
mctruth_tree.Branch('interaction_q2',interaction_q2,"interaction_q2/D")
mctruth_tree.Branch('interaction_pt',interaction_pt,"interaction_pt/D")
mctruth_tree.Branch('interaction_theta',interaction_theta,"interaction_theta/D")

particle_tree = ROOT.TTree("particle_tree","MCParticle Tree")
particle_tree.Branch("run",run,"run/i")
particle_tree.Branch("event",event,"event/i")
particle_tree.Branch('truth_index',truth_index,"truth_index/i")
particle_tree.Branch('p_index',p_index,"p_index/i")
particle_tree.Branch('status',status,"status/I")
particle_tree.Branch('trackid',trackid,"trackid/I")
particle_tree.Branch('pdgcode',pdgcode,"pdgcode/I")
particle_tree.Branch('mother',mother,"mother/I")
particle_tree.Branch('process',process)
particle_tree.Branch('endprocess',endprocess)
#particle_tree.Branch('daughters',daughters)
particle_tree.Branch('weight',weight,"weight/D")
particle_tree.Branch('rescatter',rescatter,"rescatter/I")

particle_tree.Branch('start_x',start_x,"start_x/D")
particle_tree.Branch('start_y',start_y,"start_y/D")
particle_tree.Branch('start_z',start_z,"start_z/D")
particle_tree.Branch('start_t',start_t,"start_t/D")

particle_tree.Branch('end_x',end_x,"end_x/D")
particle_tree.Branch('end_y',end_y,"end_y/D")
particle_tree.Branch('end_z',end_z,"end_z/D")
particle_tree.Branch('end_t',end_t,"end_t/D")

particle_tree.Branch('px',px,"px/D")
particle_tree.Branch('py',py,"py/D")
particle_tree.Branch('pz',pz,"pz/D")
particle_tree.Branch('p',p,"p/D")
particle_tree.Branch('pt',pt,"pt/D")
particle_tree.Branch('e',e,"e/D")
particle_tree.Branch('mass',mass,"mass/D")

particle_tree.Branch('end_px',end_px,"end_px/D")
particle_tree.Branch('end_py',end_py,"end_py/D")
particle_tree.Branch('end_pz',end_pz,"end_pz/D")
particle_tree.Branch('end_e',end_e,"end_e/D")


# In[4]:


def fill_mcparticle_info(part):
    status[0] = part.StatusCode()
    trackid[0] = part.TrackId()
    pdgcode[0] = part.PdgCode()
    mother[0] = part.Mother()
    
    process.replace(0,ROOT.string.npos, part.Process())
    endprocess.replace(0,ROOT.string.npos, part.EndProcess())
    
    #daughters.resize(part.NumberDaughters())
    #for i in range(0,daughters.size()):
    #    daughters[i] = part.Daughter(i)
    
    weight[0] = part.Weight()
    rescatter[0] = part.Rescatter()
    
    start_x[0] = part.Vx()
    start_y[0] = part.Vy()
    start_z[0] = part.Vz()
    start_t[0] = part.T()
    
    end_x[0] = part.EndX()
    end_y[0] = part.EndY()
    end_z[0] = part.EndZ()
    end_t[0] = part.EndT()
    
    px[0] = part.Px()
    py[0] = part.Py()
    pz[0] = part.Pz()
    p[0] = part.P()
    pt[0] = part.Pt()
    e[0] = part.E()
    mass[0] = part.Mass()
    
    end_px[0] = part.EndPx()
    end_py[0] = part.EndPy()
    end_pz[0] = part.EndPz()
    end_e[0] = part.EndE()
    
def fill_mctruth_info(truth):
    n_particles[0] = truth.NParticles()
    origin[0] = truth.Origin()
    
    nu = truth.GetNeutrino()
    mode[0] = nu.Mode()
    interaction_type[0] = nu.InteractionType()
    ccnc[0] = nu.CCNC()
    target[0] = nu.Target()
    hit_nucl[0] = nu.HitNuc()
    hit_quark[0] = nu.HitQuark()
    hadronic_mass[0] = nu.W()
    interaction_x[0] = nu.X()
    interaction_y[0] = nu.Y()
    interaction_q2[0] = nu.QSqr()
    interaction_pt[0] = nu.Pt()
    interaction_theta[0] = nu.Theta()
    
def fill_event_info(ev):
    run[0] = ev.eventAuxiliary().run()
    event[0] = ev.eventAuxiliary().event()


# In[5]:


mctruths_tag = art.InputTag("generator");
#filename = "/Users/wketchum/MicroBooNE_Data/genie_studies/genie_uboone_100k.root"

filenames = ROOT.vector(ROOT.string)()
for line in open("filelist.txt"):
    filenames.push_back(line.strip())

ev = gallery.Event(filenames)

get_mctruths = ev.getValidHandle(ROOT.vector(simb.MCTruth))

while (not ev.atEnd()):
    fill_event_info(ev)
    
    mctruths = get_mctruths(mctruths_tag)
    for i_t in range(0,mctruths.size()):
        truth_index[0] = i_t
        fill_mctruth_info(mctruths.product()[i_t])
        mctruth_tree.Fill()
        
        for i_p in range(0,n_particles[0]):
            p_index[0] = i_p
            fill_mcparticle_info(mctruths.product()[i_t].GetParticle(i_p))
            particle_tree.Fill()

    ev.next()


# In[6]:


outfile.cd()
mctruth_tree.Write()
particle_tree.Write()
outfile.Close()


# In[ ]:




