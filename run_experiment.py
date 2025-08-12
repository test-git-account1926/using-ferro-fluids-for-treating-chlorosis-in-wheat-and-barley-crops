#!/usr/bin/env python3
"""
Execute the ferrofluid bioavailability experiment
"""

import sys
import os
from pathlib import Path

# Add the experiment directory to Python path
experiment_dir = Path(__file__).parent / "experiments" / "ferrofluid_bioavail_001" / "run"
sys.path.insert(0, str(experiment_dir))

# Change to the experiment directory
os.chdir(str(experiment_dir))

# Import and run the experiment
from experiment import simulate_experiment, save_results, calculate_summary_stats
from datetime import datetime

if __name__ == "__main__":
    print("Running Ferrofluid Bioavailability Experiment...")
    print("=" * 50)
    
    try:
        # Run simulation
        results = simulate_experiment()
        
        # Save results
        output_dir = "../data"
        save_results(results, output_dir)
        
        print(f"Experiment completed successfully!")
        print(f"Results saved to: {output_dir}")
        print(f"Total data points collected: {sum(len(v) for v in results.values())}")
        
        # Display key findings
        summary = calculate_summary_stats(results)
        print("\nKey Findings:")
        print("-" * 30)
        for treatment, improvement in summary['iron_improvement_vs_fe_eddha_percent'].items():
            print(f"{treatment}: {improvement:+.1f}% vs Fe-EDDHA")
            
        print("\nExperiment execution completed successfully!")
        
    except Exception as e:
        print(f"Error running experiment: {e}")
        sys.exit(1)