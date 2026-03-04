"""
CSS Styles for MNIST Digit Recognition App
===========================================
Clean, modular CSS with only necessary styles.
"""

CSS = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@300;400;500;600;700&family=JetBrains+Mono:wght@400;500;600&display=swap');

* { font-family: 'Space Grotesk', sans-serif; }
code, .mono { font-family: 'JetBrains Mono', monospace; }

:root {
    --neon-green: #00ff88;
    --neon-blue: #0088ff;
    --neon-teal: #00d4aa;
    --bg-primary: #020a0a;
    --bg-card: rgba(5, 25, 25, 0.85);
    --bg-glass: rgba(0, 255, 136, 0.03);
    --text-primary: #ffffff;
    --text-secondary: #8892b0;
    --text-dim: #4a6868;
    --gradient-primary: linear-gradient(135deg, #00ff88 0%, #00d4aa 50%, #0088ff 100%);
}

/* ===== APP BACKGROUND ===== */
.stApp {
    background: var(--bg-primary);
    background-image: 
        radial-gradient(ellipse 80% 50% at 50% -20%, rgba(0, 255, 136, 0.12), transparent),
        radial-gradient(ellipse 60% 40% at 80% 50%, rgba(0, 212, 170, 0.1), transparent),
        radial-gradient(ellipse 50% 30% at 20% 80%, rgba(0, 136, 255, 0.08), transparent);
}

.stApp::before {
    content: '';
    position: fixed;
    inset: 0;
    background-image: 
        linear-gradient(rgba(0, 255, 136, 0.02) 1px, transparent 1px),
        linear-gradient(90deg, rgba(0, 255, 136, 0.02) 1px, transparent 1px);
    background-size: 50px 50px;
    pointer-events: none;
    z-index: 0;
}

[data-testid="stMainBlockContainer"] {
    padding: 1.5rem 4rem;
    position: relative;
    z-index: 1;
}

/* Hide Streamlit Elements */
header[data-testid="stHeader"] { background: transparent; }
#MainMenu, footer, .stDeployButton { display: none !important; }

/* ===== HEADER ===== */
.header {
    text-align: center;
    padding: 2rem 0 2.5rem;
}

.header-title {
    font-size: 2.5rem;
    font-weight: 700;
    margin: 0;
    letter-spacing: -0.02em;
    background: var(--gradient-primary);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    text-shadow: 0 0 80px rgba(0, 255, 136, 0.4);
}

.header-model-stats {
    display: flex;
    justify-content: center;
    gap: 2rem;
    margin-top: 1.5rem;
    flex-wrap: wrap;
}

.header-stat {
    display: flex;
    align-items: center;
    gap: 0.5rem;
    padding: 0.5rem 1rem;
    background: var(--bg-card);
    border: 1px solid rgba(0, 255, 136, 0.15);
    border-radius: 50px;
}

.header-stat-label {
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.65rem;
    color: var(--text-dim);
    text-transform: uppercase;
    letter-spacing: 0.05em;
}

.header-stat-value {
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.8rem;
    font-weight: 600;
    color: var(--neon-green);
}

/* ===== LABELS ===== */
.section-label {
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.85rem;
    font-weight: 600;
    color: var(--neon-green);
    text-transform: uppercase;
    letter-spacing: 0.12em;
    margin: 0 0 1rem 0;
    padding-bottom: 0.5rem;
    border-bottom: 1px solid rgba(0, 255, 136, 0.2);
}

.step-label {
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.7rem;
    color: var(--text-secondary);
    text-transform: uppercase;
    letter-spacing: 0.08em;
    margin: 0 0 0.75rem 0;
    padding: 0.4rem 0.8rem;
    background: rgba(0, 255, 136, 0.06);
    border-left: 3px solid var(--neon-green);
    border-radius: 0 6px 6px 0;
    display: inline-block;
}

.step-label .step-num {
    color: var(--neon-green);
    font-weight: 700;
    margin-right: 0.5rem;
}

/* ===== CANVAS ===== */
[data-testid="stCustomComponentV1"] {
    border: 2px solid var(--neon-green) !important;
    border-radius: 12px;
    overflow: visible;
    box-shadow: 0 0 40px rgba(0, 255, 136, 0.2);
    padding: .5rem;
    background-color: #0a0a1a;
    max-width: 300px;
    height: 350px;
    display: block;
}

[data-testid="stCustomComponentV1"] > div {
    border-radius: 10px !important;
    overflow: hidden;
}

/* ===== IMAGE PREVIEW ===== */
[data-testid="stImage"] {
    border-radius: 12px;
    overflow: hidden;
    border: 2px solid var(--neon-green);
    box-shadow: 0 0 40px rgba(0, 255, 136, 0.2);
}

[data-testid="stImage"] img {
    width: 280px !important;
    height: 280px !important;
    object-fit: contain;
    image-rendering: pixelated;
    background: #0a0a1a;
}

.preview-placeholder {
    width: 280px;
    height: 280px;
    border: 2px dashed rgba(0, 255, 136, 0.4);
    border-radius: 12px;
    background: linear-gradient(135deg, rgba(0, 255, 136, 0.02) 0%, rgba(0, 212, 170, 0.02) 100%);
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    color: var(--text-dim);
    font-size: 0.75rem;
    gap: 0.5rem;
    transition: all 0.3s ease;
}

.preview-placeholder:hover {
    border-color: rgba(0, 255, 136, 0.6);
    background: rgba(0, 255, 136, 0.04);
}

/* ===== FLOW ARROWS ===== */
.flow-arrow {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    height: 350px;
    color: var(--neon-green);
    margin: 0 auto;
    padding-top: 30px;
}

.flow-arrow-icon {
    font-size: 3.5rem;
    animation: arrowPulse 2s ease-in-out infinite;
    text-shadow: 0 0 40px rgba(0, 255, 136, 0.7);
    background: var(--gradient-primary);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    filter: drop-shadow(0 0 15px rgba(0, 255, 136, 0.4));
}

.flow-arrow-label {
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.6rem;
    color: var(--neon-green);
    text-transform: uppercase;
    letter-spacing: 0.1em;
    margin-top: 0.5rem;
    padding: 0.3rem 0.6rem;
    background: rgba(0, 255, 136, 0.1);
    border-radius: 6px;
    border: 1px solid rgba(0, 255, 136, 0.3);
    white-space: nowrap;
    font-weight: 600;
}

@keyframes arrowPulse {
    0%, 100% { opacity: 0.7; transform: translateX(0) scale(1); }
    50% { opacity: 1; transform: translateX(5px) scale(1.1); }
}

/* ===== RESULT DISPLAY ===== */
.result-display {
    text-align: center;
    padding: 1.5rem 1rem;
    background: var(--bg-card);
    border: 1px solid rgba(0, 255, 136, 0.15);
    border-radius: 16px;
    box-shadow: 0 0 40px rgba(0, 255, 136, 0.08);
    position: relative;
    overflow: hidden;
}

.result-display::before {
    content: '';
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    height: 2px;
    background: var(--gradient-primary);
}

.result-digit {
    font-family: 'JetBrains Mono', monospace;
    font-size: 7rem;
    font-weight: 800;
    line-height: 1;
    margin: 0;
    background: var(--gradient-primary);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    filter: drop-shadow(0 0 40px rgba(0, 255, 136, 0.6));
    animation: digitGlow 2.5s ease-in-out infinite;
    text-shadow: 0 0 60px rgba(0, 255, 136, 0.3);
}

@keyframes digitGlow {
    0%, 100% { filter: drop-shadow(0 0 20px rgba(0, 255, 136, 0.4)); }
    50% { filter: drop-shadow(0 0 40px rgba(0, 212, 170, 0.5)); }
}

.result-label {
    font-size: 0.75rem;
    color: var(--text-secondary);
    text-transform: uppercase;
    letter-spacing: 0.1em;
    margin: 0.5rem 0;
}

.result-confidence { margin-top: 0.75rem; }

.conf-badge {
    display: inline-block;
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.7rem;
    font-weight: 600;
    color: #000;
    background: var(--gradient-primary);
    padding: 0.4rem 0.8rem;
    border-radius: 20px;
    text-transform: uppercase;
    letter-spacing: 0.05em;
}

/* ===== WAITING STATE ===== */
.waiting-state {
    text-align: center;
    padding: 2rem 1rem;
    min-height: 200px;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    background: var(--bg-card);
    border: 1px dashed rgba(0, 255, 136, 0.2);
    border-radius: 16px;
}

.waiting-icon {
    font-size: 2.5rem;
    margin-bottom: 0.75rem;
    opacity: 0.4;
    filter: grayscale(0.3);
}

.waiting-text {
    color: var(--text-dim);
    font-size: 0.8rem;
    line-height: 1.6;
}

.waiting-text strong {
    color: var(--neon-green);
    font-weight: 600;
}

/* ===== BUTTONS ===== */
.stButton > button {
    background: linear-gradient(90deg, #7dffcc, #00ff88, #00e0a0);
    color: #000;
    border: none;
    font-family: 'Space Grotesk', sans-serif;
    font-weight: 700;
    font-size: 1rem;
    padding: 1rem 2.5rem;
    border-radius: 14px;
    transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
    box-shadow: 
        0 4px 20px rgba(0, 255, 136, 0.35),
        0 0 40px rgba(0, 255, 136, 0.15),
        inset 0 1px 0 rgba(255, 255, 255, 0.2);
    text-transform: uppercase;
    letter-spacing: 0.08em;
    position: relative;
    overflow: hidden;
}

.stButton > button::before {
    content: '';
    position: absolute;
    top: 0;
    left: -100%;
    width: 100%;
    height: 100%;
    background: linear-gradient(90deg, transparent, rgba(255,255,255,0.3), transparent);
    transition: left 0.5s;
}

.stButton > button:hover {
    transform: translateY(-4px) scale(1.02);
    box-shadow: 
        0 8px 30px rgba(0, 255, 136, 0.5),
        0 0 60px rgba(0, 255, 136, 0.25),
        inset 0 1px 0 rgba(255, 255, 255, 0.3);
}

.stButton > button:hover::before { left: 100%; }
.stButton > button:active { transform: translateY(-2px) scale(1.01); }

/* ===== PROBABILITY BARS ===== */
.prob-distribution {
    margin-top: 1rem;
    padding: 1rem;
    background: var(--bg-card);
    border-radius: 12px;
    border: 1px solid rgba(0, 255, 136, 0.1);
}

.prob-title {
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.7rem;
    color: var(--text-dim);
    text-transform: uppercase;
    letter-spacing: 0.1em;
    margin: 0 0 1rem 0;
}

.prob-row {
    display: flex;
    align-items: center;
    gap: 0.75rem;
    margin-bottom: 0.4rem;
}

.prob-digit {
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.75rem;
    font-weight: 500;
    color: var(--text-secondary);
    width: 1rem;
    text-align: center;
}

.prob-digit.predicted {
    color: var(--neon-green);
    font-weight: 700;
}

.prob-bar-track {
    flex: 1;
    height: 6px;
    background: rgba(255, 255, 255, 0.08);
    border-radius: 3px;
    overflow: hidden;
}

.prob-bar-fill {
    height: 100%;
    background: var(--text-dim);
    border-radius: 3px;
    transition: width 0.4s ease-out;
}

.prob-bar-fill.predicted {
    background: var(--gradient-primary);
    box-shadow: 0 0 10px rgba(0, 255, 136, 0.3);
}

.prob-value {
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.65rem;
    color: var(--text-dim);
    width: 3rem;
    text-align: right;
}

/* ===== PIPELINE WIDGET ===== */
.pipeline-widget {
    background: var(--bg-card);
    border: 1px solid rgba(0, 255, 136, 0.15);
    border-radius: 16px;
    padding: 1.5rem 2rem;
    margin: 2rem 0;
}

.pipeline-title {
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.75rem;
    color: var(--neon-green);
    text-transform: uppercase;
    letter-spacing: 0.15em;
    margin-bottom: 1.25rem;
    text-align: center;
    font-weight: 600;
}

.pipeline-steps {
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 0.35rem;
}

.pipeline-step {
    display: flex;
    flex-direction: row;
    align-items: center;
    gap: 0.75rem;
    padding: 0.6rem 1.25rem;
    background: rgba(0, 255, 136, 0.04);
    border: 1px solid rgba(0, 255, 136, 0.1);
    border-radius: 10px;
    min-width: 180px;
    transition: all 0.3s ease;
}

.pipeline-step:hover {
    border-color: rgba(0, 255, 136, 0.3);
    background: rgba(0, 255, 136, 0.08);
}

.pipeline-icon {
    font-size: 1.25rem;
}

.pipeline-step-name {
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.65rem;
    font-weight: 600;
    color: var(--text-primary);
    text-transform: uppercase;
    letter-spacing: 0.05em;
}

.pipeline-step-desc {
    font-size: 0.55rem;
    color: var(--text-dim);
    margin-left: auto;
}

.pipeline-connector {
    font-size: 0.9rem;
    color: var(--neon-green);
    opacity: 0.5;
    line-height: 1;
}

/* ===== MODEL ARCHITECTURE WIDGET ===== */
.arch-widget {
    background: var(--bg-card);
    border: 1px solid rgba(0, 255, 136, 0.15);
    border-radius: 16px;
    padding: 1.5rem 2rem;
    margin: 2rem 0;
}

.arch-title {
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.75rem;
    color: var(--neon-green);
    text-transform: uppercase;
    letter-spacing: 0.15em;
    margin-bottom: 1.25rem;
    text-align: center;
    font-weight: 600;
}

.arch-layers {
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 0.35rem;
}

.arch-layer {
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 0.4rem;
    padding: 0.6rem 1.5rem;
    background: rgba(0, 255, 136, 0.04);
    border: 1px solid rgba(0, 255, 136, 0.1);
    border-radius: 8px;
    min-width: 140px;
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.7rem;
    font-weight: 600;
    color: var(--text-primary);
    transition: all 0.3s ease;
}

.arch-layer:hover {
    border-color: rgba(0, 255, 136, 0.3);
    background: rgba(0, 255, 136, 0.08);
}

.arch-layer.arch-header {
    background: var(--gradient-primary);
    border: none;
    color: #0a0f0d;
    font-weight: 700;
    padding: 0.5rem 1.25rem;
    font-size: 0.65rem;
    letter-spacing: 0.1em;
}

.arch-layer.arch-output {
    border-color: rgba(0, 255, 136, 0.4);
    background: rgba(0, 255, 136, 0.12);
}

.arch-param {
    color: var(--neon-green);
    font-weight: 400;
    opacity: .5;
}

.arch-arrow {
    color: var(--neon-green);
    opacity: 0.5;
    font-size: 0.8rem;
    line-height: 1;
}

.arch-block {
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 0.25rem;
    padding: 0.75rem 1rem;
    background: rgba(0, 255, 136, 0.02);
    border: 1px dashed rgba(0, 255, 136, 0.15);
    border-radius: 12px;
    position: relative;
}

.arch-block-label {
    position: absolute;
    top: -0.5rem;
    left: 50%;
    transform: translateX(-50%);
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.55rem;
    font-weight: 600;
    color: var(--neon-green);
    background: var(--bg-card);
    padding: 0.1rem 0.5rem;
    border-radius: 4px;
    text-transform: uppercase;
    letter-spacing: 0.08em;
}

.arch-block .arch-layer {
    min-width: 160px;
    font-size: 0.6rem;
    padding: 0.4rem 1rem;
}

/* ===== FOOTER ===== */
.footer {
    text-align: center;
    padding: 3rem 0 2rem;
    margin-top: 3rem;
    border-top: 1px solid rgba(0, 255, 136, 0.1);
}

.credits { margin-bottom: 1.5rem; }

.credits-name {
    font-size: 1.1rem;
    font-weight: 600;
    margin: 0 0 1rem 0;
    background: var(--gradient-primary);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
}

.social-links {
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 1.5rem;
    flex-wrap: wrap;
}

.social-link {
    display: inline-flex;
    align-items: center;
    gap: 0.5rem;
    padding: 0.5rem 1rem;
    background: var(--bg-glass);
    border: 1px solid rgba(0, 255, 136, 0.15);
    border-radius: 50px;
    color: var(--text-secondary);
    text-decoration: none;
    font-size: 0.8rem;
    font-weight: 500;
    transition: all 0.3s ease;
}

.social-link:hover {
    border-color: var(--neon-green);
    color: var(--neon-green);
    background: rgba(0, 255, 136, 0.05);
    transform: translateY(-2px);
    box-shadow: 0 4px 20px rgba(0, 255, 136, 0.2);
}

.social-link svg { opacity: 0.8; }
.social-link:hover svg { opacity: 1; }

/* ===== RESPONSIVE ===== */
@media (max-width: 1024px) {
    .header-title { font-size: 2rem; }
    .result-digit { font-size: 5.5rem; }
    [data-testid="stMainBlockContainer"] { padding: 1rem 2rem; }
}

@media (max-width: 768px) {
    .header-title { font-size: 1.75rem; }
    .result-digit { font-size: 4.5rem; }
    [data-testid="stMainBlockContainer"] { padding: 1rem; }
    .social-links { gap: 0.75rem; }
    .social-link { padding: 0.4rem 0.75rem; font-size: 0.7rem; }
}

@media (max-width: 480px) {
    .header-title { font-size: 1.5rem; }
    .result-digit { font-size: 3.5rem; }
}

@media print {
    .stApp { background: white !important; }
    .stApp::before { display: none; }
}
</style>
"""
