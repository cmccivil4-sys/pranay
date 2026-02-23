class BillingService:
    COST_MAP = {
        'voice_tutor_stream': 2,
        'cv_scan': 5,
        'exam_prediction': 3,
    }

    async def consume(self, wallet_balance: int, feature: str) -> dict:
        cost = self.COST_MAP.get(feature, 1)
        if wallet_balance < cost:
            return {'allowed': False, 'balance': wallet_balance, 'cost': cost}
        return {'allowed': True, 'balance': wallet_balance - cost, 'cost': cost}


billing_service = BillingService()
