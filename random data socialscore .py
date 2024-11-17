from socialScore import SocialScoreCalculator
from typing import Dict, Union
from dataclasses import dataclass
import random
import pandas as pd
import matplotlib.pyplot as plt

# First copy all the dataclass definitions from the original code
@dataclass
class EngagementMetrics:
    engagement_rate: float
    interaction_quality: float
    growth_rate: float

@dataclass
class ContentQuality:
    frequency: float
    originality: float
    diversity: float

@dataclass
class Trustworthiness:
    trust_score: float
    verified_followers: float
    reputation_index: float

@dataclass
class SocialImpact:
    network_influence: float
    trend_setting: float
    mentions_reposts: float

@dataclass
class MonetizationPotential:
    token_transactions: float
    crowdfunding: float
    endorsement_success: float

@dataclass
class GovernanceParticipation:
    voting_activity: float
    proposal_contribution: float

def generate_sample_user_data(user_count: int) -> list:
    """Generate sample user data for demonstration purposes."""
    users = []
    
    for i in range(user_count):
        # Generate somewhat realistic data with some correlation between metrics
        base_quality = random.uniform(0.3, 0.9)  # Base quality factor for correlation
        
        # Generate user data with some realistic constraints and correlations
        user = {
            'user_id': f'user_{i+1}',
            'engagement': EngagementMetrics(
                engagement_rate=min(1.0, base_quality + random.uniform(-0.2, 0.2)),
                interaction_quality=min(1.0, base_quality + random.uniform(-0.1, 0.1)),
                growth_rate=min(1.0, base_quality + random.uniform(-0.15, 0.15))
            ),
            'content': ContentQuality(
                frequency=min(1.0, base_quality + random.uniform(-0.1, 0.1)),
                originality=min(1.0, base_quality + random.uniform(-0.2, 0.2)),
                diversity=min(1.0, base_quality + random.uniform(-0.15, 0.15))
            ),
            'trust': Trustworthiness(
                trust_score=min(1.0, base_quality + random.uniform(-0.1, 0.1)),
                verified_followers=min(1.0, base_quality + random.uniform(-0.2, 0.2)),
                reputation_index=min(1.0, base_quality + random.uniform(-0.15, 0.15))
            ),
            'impact': SocialImpact(
                network_influence=min(1.0, base_quality + random.uniform(-0.2, 0.2)),
                trend_setting=min(1.0, base_quality + random.uniform(-0.15, 0.15)),
                mentions_reposts=min(1.0, base_quality + random.uniform(-0.1, 0.1))
            ),
            'monetization': MonetizationPotential(
                token_transactions=min(1.0, base_quality + random.uniform(-0.2, 0.2)),
                crowdfunding=min(1.0, base_quality + random.uniform(-0.15, 0.15)),
                endorsement_success=min(1.0, base_quality + random.uniform(-0.1, 0.1))
            ),
            'governance': GovernanceParticipation(
                voting_activity=min(1.0, base_quality + random.uniform(-0.2, 0.2)),
                proposal_contribution=min(1.0, base_quality + random.uniform(-0.15, 0.15))
            )
        }
        users.append(user)
    
    return users

def analyze_social_scores(users_data: list) -> pd.DataFrame:
    """Analyze social scores for a list of users and return a DataFrame with results."""
    calculator = SocialScoreCalculator()
    results = []
    
    for user in users_data:
        # Calculate social score for each user
        score_data = calculator.calculate_social_score(
            user['engagement'],
            user['content'],
            user['trust'],
            user['impact'],
            user['monetization'],
            user['governance']
        )
        
        # Add user ID to results
        score_data['user_id'] = user['user_id']
        results.append(score_data)
    
    # Convert to DataFrame for easier analysis
    df = pd.DataFrame(results)
    return df

def visualize_results(df: pd.DataFrame) -> None:
    """Create visualizations of the social score analysis."""
    # Set style for better visualization
    plt.style.use('classic')
    
    # Create figure with a light gray background
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6))
    fig.patch.set_facecolor('#f0f0f0')
    
    # Plot 1: Distribution of social scores
    ax1.set_facecolor('white')
    n, bins, patches = ax1.hist(df['social_score'], bins=20, edgecolor='black', color='skyblue', alpha=0.7)
    ax1.set_title('Distribution of Social Scores', pad=15)
    ax1.set_xlabel('Score')
    ax1.set_ylabel('Number of Users')
    ax1.grid(True, linestyle='--', alpha=0.7)
    
    # Plot 2: Average component scores
    ax2.set_facecolor('white')
    component_scores = ['engagement_score', 'content_score', 'trust_score', 
                       'impact_score', 'monetization_score', 'governance_score']
    avg_scores = [df[score].mean() for score in component_scores]
    bars = ax2.bar(range(len(component_scores)), avg_scores, color='lightseagreen', alpha=0.7)
    
    # Add value labels on top of each bar
    for bar in bars:
        height = bar.get_height()
        ax2.text(bar.get_x() + bar.get_width()/2., height,
                f'{height:.2f}',
                ha='center', va='bottom')
    
    ax2.set_xticks(range(len(component_scores)))
    ax2.set_xticklabels([s.split('_')[0] for s in component_scores], rotation=45)
    ax2.set_title('Average Component Scores', pad=15)
    ax2.set_ylabel('Score')
    ax2.grid(True, linestyle='--', alpha=0.7)
    
    # Adjust layout and display
    plt.tight_layout()

def main():
    # Generate sample data for 100 users
    users_data = generate_sample_user_data(100)
    
    # Analyze the data
    results_df = analyze_social_scores(users_data)
    
    # Print summary statistics
    print("\nSummary Statistics:")
    print("-" * 50)
    print(f"Average Social Score: {results_df['social_score'].mean():.2f}")
    print("\nTier Distribution:")
    print(results_df['tier'].value_counts())
    print("\nComponent Score Averages:")
    for col in results_df.columns:
        if col.endswith('_score') and col != 'social_score':
            print(f"{col}: {results_df[col].mean():.2f}")
    
    # Create visualizations
    visualize_results(results_df)
    
    # Export results to CSV
    results_df.to_csv('social_score_analysis.csv', index=False)
    print("\nResults have been exported to 'social_score_analysis.csv'")

if __name__ == "__main__":
    main()
