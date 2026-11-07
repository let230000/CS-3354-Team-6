# BookBridge — Payment Feasibility Test

**Course:** CS 3354 Software Engineering
**Team:** 6
**Team Member:** Derrick Greene
**Date:** November 7, 2026
**Risk:** R2 — Payment Processor Integration

## 1. Purpose
The purpose of this test was to see if Stripe could handle textbook payments for our BookBridge project. We wanted to test an outside payment processor without collecting card information directly in BookBridge.

## 2. Test Setup
I created a Stripe sandbox for BookBridge and added a sample product called Calculus Textbook for $25.00 as a one-time purchase. I then generated a payment link and used Stripe's hosted checkout page.

The test was completed in the sandbox, so no real money was involved.

## 3. Test Steps
1. Created the BookBridge Stripe sandbox.
2. Added a Calculus Textbook for $25.00.
3. Generated a test payment link.
4. Completed a simulated purchase.
5. Checked the transaction in the Stripe Dashboard.

## 4. Test Results
The test payment was successful. Stripe displayed a confirmation, and the transaction appeared in the dashboard with a status of Succeeded.

The transaction used Stripe Link as the payment method.

## 5. Limitations and Next Steps
This test confirmed that Stripe's hosted checkout works in its sandbox. Stripe has not been integrated into the BookBridge application yet.

We still need to test how a successful payment updates a listing to Reserved, how failed or timed-out payments are handled, and whether BookBridge avoids storing card information after integration.

## 6. Conclusion
Stripe appears to be a possible payment processor for BookBridge based on this initial test. The simulated $25.00 payment succeeded, but application integration and additional tests are still needed.

## 7. Evidence
- Screenshot 1: Stripe checkout confirmation for $25.00.
- Screenshot 2: Stripe Dashboard showing the $25.00 transaction with Succeeded status.
