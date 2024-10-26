import random
from typing import List, Optional


class StonerThoughtGenerator:
    def __init__(self):
        self.fundamental_concepts = [
            # Physics & Cosmology (original concepts kept)
            "quantum entanglement", "wave-particle duality", "spacetime curvature", 
            "entropy", "dark energy", "quantum vacuum", "holographic principle",
            "many-worlds interpretation", "cosmic inflation", "emergence",
            
            # Neuroscience & Consciousness (expanded)
            "qualia", "neural correlates", "embodied cognition", "metacognition",
            "collective consciousness", "cognitive emergence", "neuroplasticity",
            "sentience", "phenomenal experience", "integrated information",
            "default mode network", "global workspace theory", "binding problem",
            "neural synchrony", "predictive processing", "consciousness threshold",
            "attention networks", "salience network", "mirror neurons",
            "consciousness gradient", "neural oscillations", "brain lateralization",
            
            # AI & Agents (new section)
            "artificial general intelligence", "emergent behavior", "reward modeling",
            "recursive self-improvement", "agent foundations", "value alignment",
            "mesa-optimization", "instrumental convergence", "embedded agency",
            "scalable oversight", "inner alignment", "learned optimization",
            "multi-agent systems", "artificial consciousness", "computational reflection",
            "mechanistic interpretability", "neural scaling laws", "agency theory",
            
            # Philosophy of Mind & Reality (expanded)
            "philosophical zombies", "hard problem of consciousness", "solipsism",
            "epistemic uncertainty", "ontological primitives", "modal realism",
            "emergent properties", "causal determinism", "philosophical naturalism",
            "panpsychism", "integrated information theory", "cognitive closure",
            "extended mind thesis", "multiple realizability", "neutral monism",
            "property dualism", "functionalism", "representationalism",
            
            # Mathematics & Logic (expanded)
            "infinite recursion", "mathematical platonism", "logical paradox",
            "incompleteness theorem", "transfinite numbers", "quantum logic",
            "mathematical universe hypothesis", "cellular automata", "chaos theory",
            "algorithmic information theory", "computational complexity",
            "formal verification", "type theory", "category theory"
        ]
        
        self.observable_phenomena = [
            # Natural Patterns (original kept)
            "fibonacci spirals", "standing waves", "crystalline structures",
            "bioelectric fields", "aurora borealis", "bioluminescence",
            "metamorphosis", "symbiosis", "emergence patterns", "self-organization",
            
            # Brain & Consciousness Phenomena (new section)
            "lucid dreaming", "synesthesia", "blindsight", "split-brain phenomena",
            "out-of-body experiences", "phantom limb sensations", "consciousness alterations",
            "flow states", "memory consolidation", "neural plasticity patterns",
            "brain rhythms", "selective attention", "binocular rivalry",
            
            # AI & Agent Phenomena (new section)
            "emergent capabilities", "scaling behaviors", "latent space organization",
            "activation patterns", "attention mechanisms", "feature visualization",
            "adversarial examples", "training dynamics", "loss landscapes",
            "reward hacking", "capability jumps", "neural manifolds",
            
            # Quantum Effects (original kept)
            "quantum tunneling", "superposition", "interference patterns",
            "quantum foam", "virtual particles", "quantum teleportation",
            
            # Cosmic Phenomena (original kept)
            "gravitational lensing", "cosmic microwave background", "black holes",
            "neutron stars", "gamma-ray bursts", "cosmic filaments",
            "galactic superclusters", "quasars", "magnetars"
        ]
        
        self.analytical_verbs = [
            # Scientific Process (expanded)
            "emerges from", "correlates with", "self-organizes into",
            "fundamentally underlies", "spontaneously generates",
            "recursively creates", "quantum tunnels through",
            "systematically processes", "adaptively learns",
            "hierarchically structures", "causally influences",
            
            # AI & Agency (new section)
            "optimizes towards", "learns to model", "generalizes across",
            "recursively improves", "internally represents",
            "abstractly reasons about", "actively explores",
            "strategically plans", "metabolizes information",
            "self-modifies through", "meta-learns from",
            
            # Consciousness & Cognition (new section)
            "consciously processes", "subjectively experiences",
            "phenomenally binds", "attentionally selects",
            "metacognitively reflects", "intentionally directs",
            "neurally encodes", "consciously integrates",
            
            # Philosophical Analysis (expanded)
            "transcends beyond", "dialectically synthesizes",
            "phenomenologically manifests", "axiomatically derives",
            "epistemically relates to", "ontologically grounds",
            "functionally implements", "computationally realizes",
            
            # Systems Thinking (expanded)
            "complexly interweaves", "dynamically equilibrates",
            "fractally iterates", "non-linearly evolves",
            "cybernetically regulates", "autopoietically maintains",
            "emergently generates", "adaptively responds"
        ]
        
        self.descriptive_adjectives = [
            # Scientific Properties (expanded)
            "quantum-entangled", "electromagnetically coherent",
            "thermodynamically irreversible", "topologically invariant",
            "computationally irreducible", "stochastically resonant",
            "neurally integrated", "informationally dense",
            
            # AI & Agent Properties (new section)
            "recursively optimal", "mechanistically interpretable",
            "algorithmically aligned", "computationally bounded",
            "agentic", "meta-learned", "self-improving",
            "capability-aware", "intentionally-directed",
            
            # Consciousness Properties (new section)
            "phenomenally conscious", "subjectively experienced",
            "metacognitively aware", "attentionally selected",
            "neurally synchronized", "consciously integrated",
            "experientially rich", "qualia-bearing",
            
            # Philosophical Qualities (expanded)
            "metaphysically necessary", "epistemologically fundamental",
            "phenomenologically direct", "ontologically primitive",
            "teleologically directed", "dialectically resolved",
            "functionally realized", "representationally grounded",
            
            # Systems Properties (expanded)
            "emergently complex", "recursively self-similar",
            "dynamically stable", "cybernetically regulated",
            "homeostatic", "auto-catalytic",
            "adaptively responsive", "hierarchically organized"
        ]
        
        # Added missing thought_starters
        self.thought_starters = [
            "Dude, what if",
            "Bro, imagine if",
            "Have you ever noticed that",
            "Hear me out, but",
            "Just realized that",
            "Maybe like",
            "Mind-blowing thought:",
            "What if I told you"
        ]
        
        self.intellectual_prompts = [
            # Scientific Inquiry (original kept)
            "Consider the implications if",
            "The evidence suggests that",
            "A fascinating consequence of this is",
            "Recent findings indicate",
            "The paradox arises when",
            
            # AI & Consciousness Inquiry (new section)
            "The training dynamics reveal that",
            "The neural architecture suggests",
            "The emergence pattern indicates",
            "The consciousness metrics show",
            "The agent behavior implies",
            
            # Philosophical Analysis (original kept)
            "Let us examine the premise that",
            "One might reasonably argue that",
            "The fundamental question remains:",
            "A careful analysis reveals",
            "Consider the counterfactual where",
            
            # Synthesis & Integration (original kept)
            "The synthesis of these ideas suggests",
            "At the intersection of these theories lies",
            "This framework might explain how",
            "The unifying principle appears to be",
            "A more nuanced interpretation shows"
        ]
        
        self.paradigm_shifts = [
            # Original Scientific Revolutions (kept)
            "quantum mechanics overthrows classical determinism",
            "relativity redefines space and time",
            "entropy implies the arrow of time",
            "evolution challenges essentialism",
            
            # AI & Consciousness Revolutions (new section)
            "artificial minds challenge human uniqueness",
            "deep learning transcends symbolic AI",
            "emergence explains consciousness",
            "information processing defines cognition",
            "neural networks surpass explicit programming",
            "artificial agents develop natural language",
            "machine consciousness becomes measurable",
            
            # Philosophical Transformations (expanded)
            "mind emerges from physical processes",
            "consciousness shapes perceived reality",
            "information becomes fundamental",
            "complexity arises from simplicity",
            "agency emerges from optimization",
            "intentionality arises from computation",
            "consciousness gradients replace binary distinctions",
            
            # Interdisciplinary Insights (expanded)
            "biology meets quantum physics",
            "mathematics describes emergence",
            "information theory meets consciousness",
            "chaos theory meets free will",
            "AI meets neuroscience",
            "computation meets phenomenology",
            "agency meets optimization theory"
        ]
        
        # Original patterns
        self.philosophical_patterns = [
            "{starter} {object} is just {adjective} {concept} when you really think about it?",
            "{starter} {concept} actually {verb} through every {object} in existence?",
            "{starter} we're all just {adjective} {object} in a giant {concept}?",
            "{starter} {concept} is just {object} that {verb} on a {adjective} level?",
            "{starter} our {object} {verb} with the {adjective} {concept}?",
            "{starter} {adjective} {object} contains all the secrets of {concept}?",
            "{starter} every {object} we see is connected through {adjective} {concept}?"
        ]

        # Advanced patterns
        self.advanced_patterns = [
            "{starter} the {adjective} nature of {concept} implies that {object} {verb} in higher dimensions?",
            "{starter} {concept} is fundamentally a manifestation of {adjective} {object} that {verb} through spacetime?",
            "{starter} the observer effect means our {concept} literally {verb} the {adjective} {object}?",
            "{starter} quantum superposition allows {object} to simultaneously {verb} with multiple states of {concept}?",
            "{starter} artificial {object} could develop {adjective} {concept} that {verb} beyond human understanding?",
            "{starter} consciousness is an {adjective} property that {verb} when {object} reaches sufficient {concept}?",
            "{starter} agent consciousness emerges when {adjective} {object} learns to {verb} its own {concept}?"
        ]
        
        # No need to extend here since we'll select based on complexity
        
    def generate_thought(self, 
                        mode: str = "random", 
                        complexity: int = 1) -> str:
        """
        Generate a philosophical thought with specified mode and complexity.
        
        Args:
            mode: One of ["random", "quantum", "consciousness", "cosmic", "metaphysical"]
            complexity: 1 (basic) to 3 (most complex)
            
        Returns:
            str: A generated philosophical thought
        """
        # Filter concepts based on mode
        filtered_concepts = self.fundamental_concepts
        if mode != "random":
            mode_filters = {
                "quantum": ["quantum", "wave", "entangle", "superposition"],
                "consciousness": ["conscious", "mind", "qualia", "cognitive"],
                "cosmic": ["cosmic", "universe", "space", "galaxy"],
                "metaphysical": ["ontological", "metaphysical", "philosophical"]
            }
            
            if mode in mode_filters:
                filtered_concepts = [
                    concept for concept in self.fundamental_concepts 
                    if any(filter_word in concept.lower() for filter_word in mode_filters[mode])
                ]
        
        # Select pattern and components based on complexity
        if complexity == 1:
            patterns = self.philosophical_patterns
            starters = self.thought_starters
            verbs = self.analytical_verbs
            adjectives = self.descriptive_adjectives
        elif complexity == 2:
            patterns = self.advanced_patterns
            starters = self.intellectual_prompts
            verbs = [v for v in self.analytical_verbs if " " in v]
            adjectives = [adj for adj in self.descriptive_adjectives if "-" in adj]
        else:
            # Generate a compound thought combining multiple paradigm shifts
            shift = random.choice(self.paradigm_shifts)
            patterns = ["{starter} {concept} {verb} because " + shift + ", which means {adjective} {object} must be fundamental?"]
            starters = self.intellectual_prompts
            verbs = [v for v in self.analytical_verbs if " " in v]
            adjectives = [adj for adj in self.descriptive_adjectives if "-" in adj]
        
        return "[AdvancedStonerThought™]: " + random.choice(patterns).format(
            starter=random.choice(starters),
            concept=random.choice(filtered_concepts or self.fundamental_concepts),
            object=random.choice(self.observable_phenomena),
            verb=random.choice(verbs),
            adjective=random.choice(adjectives)
        )

    def generate_philosophical_chain(self, 
                                  seed_concept: str, 
                                  length: int = 3, 
                                  complexity: int = 1) -> List[str]:
        """
        Generate a chain of related philosophical thoughts building on each other.
        
        Args:
            seed_concept: Initial concept to start the chain
            length: Number of thoughts to generate
            complexity: Base complexity level (1-3)
            
        Returns:
            List[str]: A list of connected thoughts
        """
        thoughts = []
        current_concept = seed_concept
        
        for i in range(length):
            # Increase complexity as the chain progresses
            current_complexity = min(3, complexity + (i // 2))
            
            thought = self.generate_thought(
                mode="random",
                complexity=current_complexity
            )
            thoughts.append(thought)
            
            # Use a paradigm shift to transition to the next thought
            current_concept = random.choice(self.fundamental_concepts)
            
        return thoughts

    def generate_dialectic(self, concept: str) -> List[str]:
        """
        Generate a Hegelian dialectic about a concept.
        
        Args:
            concept: The concept to analyze dialectically
            
        Returns:
            List[str]: [thesis, antithesis, synthesis]
        """
        # Generate thesis with higher complexity
        thesis = self.generate_thought(complexity=2)
        
        # Generate contrasting antithesis
        antithesis_pattern = "But what if {concept} actually {verb} in the opposite way, making {object} {adjective}?"
        antithesis = "[AdvancedStonerThought™]: " + antithesis_pattern.format(
            concept=concept,
            verb=random.choice(self.analytical_verbs),
            object=random.choice(self.observable_phenomena),
            adjective=random.choice(self.descriptive_adjectives)
        )
        
        # Generate synthesis combining both perspectives
        synthesis_pattern = "Perhaps {concept} simultaneously {verb} both the {adjective} {object} and its opposite?"
        synthesis = "[AdvancedStonerThought™]: " + synthesis_pattern.format(
            concept=concept,
            verb=random.choice(self.analytical_verbs),
            object=random.choice(self.observable_phenomena),
            adjective=random.choice(self.descriptive_adjectives)
        )
        
        return [thesis, antithesis, synthesis]

    def generate_interdisciplinary_insight(self, 
                                        field1: str, 
                                        field2: str) -> str:
        """
        Generate a thought connecting concepts from two different fields.
        
        Args:
            field1: First field of study
            field2: Second field of study
            
        Returns:
            str: An insight connecting both fields
        """
        # Filter concepts from each field
        concepts1 = [c for c in self.fundamental_concepts if field1.lower() in c.lower()]
        concepts2 = [c for c in self.fundamental_concepts if field2.lower() in c.lower()]
        
        if not (concepts1 and concepts2):
            return self.generate_thought()  # Fallback if no matching concepts
            
        pattern = "What if {concept1} and {concept2} are both manifestations of {adjective} {object} that {verb}?"
        
        return "[AdvancedStonerThought™]: " + pattern.format(
            concept1=random.choice(concepts1),
            concept2=random.choice(concepts2),
            adjective=random.choice(self.descriptive_adjectives),
            object=random.choice(self.observable_phenomena),
            verb=random.choice(self.analytical_verbs)
        )

    def add_custom_paradigm(self, 
                          paradigm: str, 
                          category: Optional[str] = None) -> None:
        """
        Add a new paradigm shift to the collection.
        
        Args:
            paradigm: New paradigm shift to add
            category: Optional category for organization
        """
        if category and category not in ["Scientific Revolutions", 
                                       "Philosophical Transformations",
                                       "Interdisciplinary Insights"]:
            raise ValueError("Invalid paradigm category")
            
        self.paradigm_shifts.append(paradigm)

    def get_categories(self) -> List[str]:
        """
        Return all available word categories.
        
        Returns:
            List[str]: List of category names
        """
        return [attr for attr in dir(self) 
                if isinstance(getattr(self, attr), list) 
                and not attr.startswith('_')]

    def get_random_thought(self, eager: bool = False) -> Optional[str]:
        """
        Generate a random intrusive thought with random parameters.
        Has a chance to not generate anything unless eager=True.
        
        Args:
            eager: If True, always generates a thought. If False, has a 30% chance to generate nothing
                (simulating the random nature of intrusive thoughts)
        
        Returns:
            Optional[str]: A random thought, or None if no thought was generated
        """
        # Only generate a thought 30% of the time unless eager=True
        if not eager and random.random() > 0.3:
            return None
            
        # Randomly select mode
        modes = ["random", "quantum", "consciousness", "cosmic", "metaphysical"]
        mode = random.choice(modes)
        
        # Complexity weighted towards simpler thoughts
        complexity_weights = [0.5, 0.3, 0.2]  # 50% chance of complexity 1, 30% chance of 2, 20% chance of 3
        complexity = random.choices([1, 2, 3], weights=complexity_weights)[0]
        
        # Randomly decide whether to generate a special type of thought
        thought_type = random.choices(
            ["normal", "dialectic", "chain", "interdisciplinary"],
            weights=[0.7, 0.1, 0.1, 0.1]  # 70% normal thoughts, 10% each for special types
        )[0]
        
        if thought_type == "normal":
            return self.generate_thought(mode=mode, complexity=complexity)
        elif thought_type == "dialectic":
            return random.choice(self.generate_dialectic(random.choice(self.fundamental_concepts)))
        elif thought_type == "chain":
            return random.choice(self.generate_philosophical_chain(
                random.choice(self.fundamental_concepts),
                length=2,
                complexity=complexity
            ))
        else:  # interdisciplinary
            fields = ["quantum", "consciousness", "physics", "mathematics", "philosophy", "biology"]
            field1, field2 = random.sample(fields, 2)
            return self.generate_interdisciplinary_insight(field1, field2)


if __name__ == "__main__":

    # Create an instance of the generator
    generator = StonerThoughtGenerator()

    # 1. Basic thought generation with different complexity levels
    print("\n=== Basic Thoughts ===")
    print("\nComplexity 1 (Basic):")
    print(generator.generate_thought(complexity=1))

    print("\nComplexity 2 (Advanced):")
    print(generator.generate_thought(complexity=2))

    print("\nComplexity 3 (Complex):")
    print(generator.generate_thought(complexity=3))

    # 2. Generate thoughts in different modes
    print("\n=== Different Modes ===")
    modes = ["quantum", "consciousness", "cosmic", "metaphysical"]
    for mode in modes:
        print(f"\n{mode.title()} Mode:")
        print(generator.generate_thought(mode=mode, complexity=2))

    # 3. Generate a philosophical chain
    print("\n=== Philosophical Chain ===")
    seed_concept = "consciousness"
    thoughts = generator.generate_philosophical_chain(
        seed_concept=seed_concept,
        length=3,
        complexity=2
    )
    print(f"\nPhilosophical chain starting with '{seed_concept}':")
    for i, thought in enumerate(thoughts, 1):
        print(f"\n{i}. {thought}")

    # 4. Generate a dialectic
    print("\n=== Hegelian Dialectic ===")
    concept = "quantum consciousness"
    dialectic = generator.generate_dialectic(concept)
    print(f"\nDialectic about '{concept}':")
    for thought in dialectic:
        print(f"\n{thought}")

    # 5. Generate interdisciplinary insights
    print("\n=== Interdisciplinary Insights ===")
    field_pairs = [
        ("quantum", "consciousness"),
        ("mathematics", "philosophy"),
        ("physics", "biology")
    ]
    for field1, field2 in field_pairs:
        print(f"\nConnecting {field1} and {field2}:")
        print(generator.generate_interdisciplinary_insight(field1, field2))

    # 6. Add and use a custom paradigm
    print("\n=== Custom Paradigm ===")
    generator.add_custom_paradigm(
        "artificial intelligence transcends human cognition",
        "Scientific Revolutions"
    )
    print(generator.generate_thought(complexity=3))  # Might use the new paradigm


    # print 500 random thoughts
    print("\n=== Random Thoughts ===")
    for _ in range(500):
        thought = generator.get_random_thought()
        if thought:
            print(thought)
