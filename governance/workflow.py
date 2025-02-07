from datetime import datetime
from typing import Dict, Optional, Set

class ContractWorkflow:
    def __init__(self, contract_draft):
        self.draft = contract_draft
        self.status = "draft"
        self.approvals = {}
        
    def submit_for_review(self):
        """Soumet le contract pour revue"""
        self.status = "in_review"
        self.notify_reviewers()
        
    def approve(self, reviewer_role, comments=None):
        """Enregistre une approbation"""
        self.approvals[reviewer_role] = {
            'approved_at': datetime.now(),
            'comments': comments
        }
        
    def is_fully_approved(self):
        """Vérifie si toutes les approbations sont obtenues"""
        required_roles = {'technical', 'business', 'steward', 'owner'}
        return required_roles.issubset(self.approvals.keys())

class GovernanceMetrics:
    def calculate_adoption_rate(self):
        """Calcule le taux d'adoption des contracts"""
        return {
            'total_contracts': self.count_total_contracts(),
            'active_contracts': self.count_active_contracts(),
            'compliance_rate': self.calculate_compliance_rate(),
            'quality_score': self.calculate_quality_score()
        }
        
    def generate_governance_report(self):
        """Génère un rapport de gouvernance"""
        return {
            'metrics': self.calculate_adoption_rate(),
            'violations': self.get_contract_violations(),
            'pending_reviews': self.get_pending_reviews(),
            'quality_trends': self.analyze_quality_trends()
        } 