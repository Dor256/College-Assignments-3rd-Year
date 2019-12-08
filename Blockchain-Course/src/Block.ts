import SHA256 from "crypto-js/sha256";
import { Transaction } from "./Transaction";

export type Data = {
    amount: number;
}

export class Block {
    private timestamp: string;
    private _transactions: Transaction[];
    private _previousHash: string;
    private _hash: string;
    private _nonce: number;

    constructor(timestamp: string, transactions: Transaction[], previousHash: string = '') {
        this.timestamp = timestamp;
        this._transactions = transactions;
        this._previousHash = previousHash;
        this._hash = this.calculateHash();
        this._nonce = 0;
    }

    calculateHash(): string {
        return SHA256(this.previousHash + this.timestamp + JSON.stringify(this.transactions) + this.nonce).toString();
    }
    
    mineBlock(difficulty: number) {
        while(this.hash.substring(0, difficulty) !== Array(difficulty + 1).join("0")) {
            this.nonce++;
            this.hash = this.calculateHash();
        }
        console.log(`Block Mined: ${this.hash}`);
    }

    get previousHash(): string {
        return this._previousHash;
    }

    set previousHash(previousHash: string) {
        this._previousHash = previousHash;
    }

    get hash(): string {
        return this._hash;
    }

    set hash(hash: string) {
        this._hash = hash;
    }

    get nonce(): number {
        return this._nonce;
    }

    set nonce(nonce: number) {
        this._nonce = nonce;
    }

    get transactions(): Transaction[] {
        return this._transactions;
    }
}
