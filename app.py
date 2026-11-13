from pathlib import Path

import streamlit as st

ROOT = Path(__file__).parent
ASSETS = ROOT / "assets"

st.set_page_config(page_title="EliteDesign | RNA Design", page_icon="🧬", layout="wide", initial_sidebar_state="collapsed")

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=Space+Grotesk:wght@500;600;700&display=swap');
:root { --ink:#18251f; --muted:#607068; --green:#28734d; --mint:#dff5e9; --paper:#f6f8f3; }
.stApp { background:var(--paper); color:var(--ink); font-family:'DM Sans',sans-serif; }
.block-container { width:92vw; max-width:1800px; padding-top:4.75rem; padding-bottom:3rem; }
a { text-decoration:none !important; }
.nav { display:flex; align-items:center; justify-content:space-between; padding:.5rem 0 2.75rem; }
.brand { font-family:'Space Grotesk'; font-weight:700; font-size:2rem; }
.tag { font-size:1.5rem; letter-spacing:.08em; text-transform:uppercase; color:var(--green); font-weight:700; }
.hero-title { font-family:'Space Grotesk'; font-weight:700; font-size:clamp(3rem,6.5vw,6.25rem); line-height:.94; letter-spacing:-.065em; margin:.55rem 0 1.4rem; max-width:1000px; overflow-wrap:normal; }
.hero-title span { color:var(--green); }
.hero-copy { font-size:clamp(1.5rem,1.5vw,2rem) !important; line-height:1.5 !important; color:var(--muted); max-width:1200px; margin:0 0 2.1rem; font-weight:600 !important; }
.buttons { display:flex; flex-wrap:wrap; gap:.7rem; }
.button { display:inline-block; border:1px solid #bcc9c1; border-radius:999px; padding:1.25rem 1.9rem; color:var(--ink)!important; font-size:1.7rem; font-weight:700; }
.button.primary { background:var(--ink); color:white!important; border-color:var(--ink); }
.profile-links { display:flex; flex-wrap:wrap; gap:1.6rem; margin-top:1.6rem; color:var(--muted); font-size:1.6rem; }
.profile-links a { color:var(--green)!important; font-weight:700; }
.authors { margin-top:2rem; color:var(--muted); line-height:1.6; font-size:1.9rem; }
.authors strong { color:var(--ink); font-weight:700; }
.affiliations { color:#6f7f77; font-size:1.55rem; line-height:1.65; margin-top:.7rem; max-width:1650px; }
.metric-grid { display:grid; grid-template-columns:repeat(3,1fr); gap:1rem; margin:4rem 0; }
.metric { background:white; border:1px solid #e2e8e3; border-radius:18px; padding:2.2rem; }
.metric strong { font-family:'Space Grotesk'; display:block; font-size:4rem; color:var(--green); letter-spacing:-.05em; }
.metric span { color:var(--muted); font-size:1.75rem; line-height:1.5; }
.section-kicker { color:var(--green); font-weight:700; text-transform:uppercase; font-size:1.45rem; letter-spacing:.11em; margin-top:5rem; }
.section-title { font-family:'Space Grotesk'; font-size:clamp(3rem,4.5vw,4.75rem); max-width:1200px; margin:.6rem 0 2.2rem; letter-spacing:-.04em; }
.flow { display:grid; grid-template-columns:repeat(4,1fr); gap:.7rem; margin-bottom:4rem; }
.step { background:var(--mint); border-radius:18px; padding:2rem; min-height:280px; }
.step:nth-child(2),.step:nth-child(4) { background:#edf2e5; }
.num { display:inline-grid; place-items:center; width:52px; height:52px; border-radius:50%; background:var(--ink); color:white; font-size:1.4rem; font-weight:700; }
.step h3 { font-family:'Space Grotesk'; font-size:2.25rem; margin:1.4rem 0 .7rem; }
.step p { color:var(--muted); line-height:1.55; font-size:1.7rem; margin-bottom:0; }
.research-caption { color:var(--muted); line-height:1.45 !important; font-size:2.15rem !important; font-weight:600 !important; }
.figure-card { background:white; border:1px solid #e2e8e3; border-radius:22px; padding:1rem; }
.small-note { color:var(--muted); font-size:2.15rem; line-height:1.45; font-weight:600; margin:1.1rem 0 0; }
.footer-card { background:var(--ink); color:white; border-radius:24px; padding:3rem; margin-top:5rem; display:grid; grid-template-columns:minmax(0,1fr) auto; gap:2.5rem; align-items:center; overflow:hidden; }
.footer-copy { min-width:0; }
.footer-card h2 { font-family:'Space Grotesk'; color:white; margin:.45rem 0 .65rem; font-size:clamp(3rem,4vw,4.5rem); line-height:1.05; letter-spacing:-.04em; }
.footer-card p { color:#d3dcd7; margin:0; max-width:980px; font-size:1.7rem; line-height:1.55; }
.footer-actions { display:flex; flex-wrap:nowrap; justify-content:flex-end; align-items:center; gap:.75rem; max-width:none; }
.footer-link { display:inline-block; background:white; color:var(--ink)!important; border:1px solid white; border-radius:999px; padding:1.1rem 1.45rem; font-size:1.4rem; font-weight:700; white-space:nowrap; }
.comparison-label { text-align:center; font-family:'Space Grotesk'; font-size:2.3rem; line-height:1.1; font-weight:700; color:var(--ink); letter-spacing:-.03em; margin:.35rem 0 .9rem; }
.comparison-score { text-align:center; color:var(--green); font-weight:700; font-size:1.15rem; line-height:1.5; min-height:3rem; margin-bottom:.8rem; }
.legend-wrap { max-width:820px; margin:0 auto 1.5rem; }
@media(max-width:700px){.block-container{width:94vw;padding-top:4rem}.metric-grid,.flow{grid-template-columns:1fr}.nav .tag{display:none}.hero-title{font-size:clamp(2.75rem,15vw,3.7rem);line-height:.98;letter-spacing:-.055em}.hero-copy{font-size:1.4rem!important}.button{font-size:1.05rem;padding:.85rem 1.15rem}.authors{font-size:1.05rem}.affiliations{font-size:.88rem}.research-caption{font-size:1.4rem!important}.small-note{font-size:1.2rem}.footer-card{grid-template-columns:1fr;padding:1.6rem;gap:1.25rem}.footer-actions{justify-content:flex-start;flex-wrap:wrap}}
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="nav"><div class="brand">EliteDesign</div><div class="tag">RNA inverse folding · Cross-entropy optimization</div></div>
<div class="tag">Research spotlight</div>
<div class="hero-title">Designing RNA sequences<br><span>with the cross-entropy method.</span></div>
<p class="hero-copy">EliteDesign learns where promising RNA sequences live, keeps the best candidates, and rapidly concentrates its search around them.</p>
<div class="buttons"><a class="button primary" href="https://github.com/JSONFN21/EliteDesign-Paper" target="_blank">Read the paper ↗</a><a class="button" href="https://github.com/JSONFN21/EliteDesign" target="_blank">Explore the code ↗</a></div>
<div class="authors"><strong>JasonFred Ngwa<sup>1,2</sup></strong> · Milan Gautam<sup>1</sup> · David H. Mathews<sup>3</sup> · Liang Huang<sup>1,2,†</sup></div>
<div class="affiliations"><sup>1</sup> Oregon State University, School of EECS &nbsp;·&nbsp; <sup>2</sup> Oregon State University, Biochemistry &amp; Biophysics &nbsp;·&nbsp; <sup>3</sup> University of Rochester Medical Center, Center for RNA Biology &nbsp;·&nbsp; <sup>†</sup> Corresponding author</div>
<div class="profile-links"><a href="https://www.linkedin.com/in/jasonfred/" target="_blank">JasonFred on LinkedIn ↗</a><a href="https://github.com/JSONFN21" target="_blank">JasonFred on GitHub ↗</a></div>
<div class="metric-grid"><div class="metric"><strong>178×</strong><span>faster than SamplingDesign on Eterna100</span></div><div class="metric"><strong>0.52</strong><span>mean probability on long 16S-MFE targets</span></div><div class="metric"><strong>14×</strong><span>faster than SAMFEO on 16S-MFE</span></div></div>
""", unsafe_allow_html=True)

st.markdown('<div class="section-kicker">The idea</div><h2 class="section-title">A simple loop that learns from the elite.</h2>', unsafe_allow_html=True)
st.markdown("""
<div class="flow">
<div class="step"><span class="num">1</span><h3>Sample</h3><p>Draw valid RNA sequences from the current distribution.</p></div>
<div class="step"><span class="num">2</span><h3>Score</h3><p>Estimate how strongly each sequence favors the target fold.</p></div>
<div class="step"><span class="num">3</span><h3>Select</h3><p>Keep a small set of the highest-performing sequences.</p></div>
<div class="step"><span class="num">4</span><h3>Learn</h3><p>Move the distribution toward the elite set, then repeat.</p></div>
</div>
""", unsafe_allow_html=True)

st.markdown('<div class="section-kicker">Results</div><h2 class="section-title">Higher-quality designs as target length grows.</h2>', unsafe_allow_html=True)
left, right = st.columns([1, 1.45], gap="large")
with left:
    st.image(ASSETS / "eterna_probability.png", use_container_width=True)
    st.markdown('<p class="small-note">Mean target probability across longer Eterna100 puzzles.</p>', unsafe_allow_html=True)
with right:
    st.image(ASSETS / "runtime_scaling.png", use_container_width=True)
    st.markdown('<p class="small-note">Runtime per target across ten long 16S-MFE structures.</p>', unsafe_allow_html=True)

st.markdown('<div class="section-kicker">Designed sequences</div><h2 class="section-title">Closer to the target than SamplingDesign.</h2>', unsafe_allow_html=True)
st.markdown('<p class="hero-copy" style="max-width:1400px">A better design has less red and a folded shape that looks more like the target y*.</p>', unsafe_allow_html=True)
target, elite, sampling = st.columns(3, gap="medium")
with target:
    st.markdown('<div class="comparison-label">Target y*</div>', unsafe_allow_html=True)
    st.image(ASSETS / "comparison_target.png", use_container_width=True)
with elite:
    st.markdown('<div class="comparison-label">EliteDesign</div>', unsafe_allow_html=True)
    st.image(ASSETS / "comparison_elite.png", use_container_width=True)
with sampling:
    st.markdown('<div class="comparison-label">SamplingDesign</div>', unsafe_allow_html=True)
    st.image(ASSETS / "comparison_sampling.png", use_container_width=True)
st.markdown('<p class="research-caption" style="text-align:center;max-width:1400px;margin:1.5rem auto 0">Puzzle #90 (“Gladius”), a 400-nt target.</p>', unsafe_allow_html=True)

st.markdown("""
<div class="footer-card">
  <div class="footer-copy">
    <div class="tag" style="color:#c8ee77">Open research</div>
    <h2>Explore EliteDesign.</h2>
    <p>Read the full methods and results, or use the open-source implementation.</p>
  </div>
  <div class="footer-actions">
    <a class="footer-link" href="https://github.com/JSONFN21/EliteDesign-Paper" target="_blank">Paper ↗</a>
    <a class="footer-link" href="https://github.com/JSONFN21/EliteDesign" target="_blank">Code ↗</a>
    <a class="footer-link" href="https://www.linkedin.com/in/jasonfred/" target="_blank">LinkedIn ↗</a>
    <a class="footer-link" href="https://github.com/JSONFN21" target="_blank">GitHub ↗</a>
  </div>
</div>
""", unsafe_allow_html=True)
